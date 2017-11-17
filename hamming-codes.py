import numpy as np
# algorithm
def encode(parity_bits, data):
    n = len(data) + parity_bits
    assert 2 ** parity_bits == n + 1

    # copy data to code
    code = np.zeros(n, dtype=int)
    code[np.arange(n) & np.arange(n) + 1 > 0] = data

    # parity mask
    mask = np.zeros(n, dtype=int)
    mask[::2] = 1

    # compute parity
    i = 0
    while i < n:
        code[i] = code[i:][mask == 1].sum() & 1
        i += i + 1
        mask = np.repeat(mask, 2)[:n - i]

    # result
    return code

def decode(code):
    n = len(code)

    # parity mask
    mask = np.zeros(n, dtype=int)
    mask[::2] = 1

    # compute parity
    error, i = -1, 0
    while i < n:
        error += (i + 1) * (code[i:][mask == 1].sum() & 1)
        i += i + 1
        mask = np.repeat(mask, 2)[:n - i]

    # fix error
    if error >= 0:
        code[error] ^= 1

    # get data from code
    data = code[np.arange(n) & np.arange(n) + 1 > 0]

    # result
    return error, data
# encoding
parity_bits = 3
data = np.random.randint(0, 2, 4)

# generate code
code = encode(parity_bits, data)
print('hamming code', data, '->', code)

# make error
code[3] ^= 1
print('with error', code)

# reconstruct
error, recon = decode(code)
print('error @', error, '->', recon)

parity_bits = 4
data = np.random.randint(0, 2, 11)

# generate code
code = encode(parity_bits, data)
print('hamming code', data, '->', code)

# make error
code[14] ^= 1
print('with error', code)

# reconstruct
error, recon = decode(code)
print('error @', error, '->', recon)
