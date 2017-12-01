# algorithm
def lzw_encode(data):
    code, code_bits = {bytes([i]): i for i in range(256)}, 8
    buffer, buffer_bits = 0, 0
    index, aux = 0, []

    while index < len(data):
        # find word
        for j in range(index + 1, len(data) + 1):
            word = data[index:j]

            # store word
            if word not in code:
                code[word] = len(code)
                word = word[:-1]
                break

        # write buffer
        buffer <<= code_bits
        buffer |= code[word]
        buffer_bits += code_bits

        # code length
        if len(code) > 2 ** code_bits:
            code_bits += 1

        # shift
        index += len(word)

        # buffer alignment
        if index >= len(data) and buffer_bits % 8:
            r = 8 - (buffer_bits % 8)
            buffer <<= r
            buffer_bits += r

        # emit output
        if not buffer_bits % 8:
            aux += int.to_bytes(buffer, buffer_bits >> 3, 'big')
            buffer, buffer_bits = 0, 0

    return bytes(aux)

def lzw_decode(data):
    code, code_bits = {i: bytes([i]) for i in range(256)}, 8
    buffer, buffer_bits = 0, 0
    index, aux = 0, []
    prefix = b''

    while index < len(data) or buffer_bits >= code_bits:
        # read buffer
        while index < len(data) and buffer_bits < code_bits:
            buffer <<= 8
            buffer |= data[index]
            buffer_bits += 8
            index += 1

        # find word
        buffer_bits -= code_bits
        key = buffer >> buffer_bits
        buffer &= (1 << buffer_bits) - 1
        word = code.get(key, prefix + prefix[:1])

        # store word
        if prefix:
            code[len(code)] = prefix + word[:1]
        prefix = word

        # code length
        if len(code) >= 2 ** code_bits:
            code_bits += 1

        # emit output
        aux += word

    return bytes(aux)

# run
def compress(data):
    encoded = lzw_encode(data.encode('ASCII'))
    decoded = lzw_decode(encoded).decode('ASCII')
    assert data == decoded

    print('compression', len(data), '->', len(encoded), 'bytes')

compress('ATGATCATGAG')
compress('x' * 1000)
compress("""
I wish that I knew what I know now
When I was younger.
I wish that I knew what I know now
When I was stronger.
""")
