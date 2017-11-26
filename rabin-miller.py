from random import randrange

# algorithm
def rabin_miller(prime, tests):
    if prime < 5:
        return prime in [2, 3]

    # set: prime = q * 2**r + 1
    q, r = prime - 1, 0
    while not q & 1:
        q >>= 1
        r += 1

    # test repeatedly
    for _ in range(tests):
        a = randrange(2, prime - 1)

        # pass if: a**q == 1
        x = pow(a, q, prime)
        if x in [1, prime - 1]:
            continue

        # pass if: a**(q * 2**s) == -1, s < r
        for _ in range(r - 1):
            x = pow(x, 2, prime)
            if x == prime - 1:
                break
        else:
            return False

    return True

def prime(bits, tests):
    while True:
        # random number in [2**bits .. 2**(bits+1)-1]
        prime = (1 << bits) | randrange(1 << bits) | 1

        # primality test
        if rabin_miller(prime, tests):
            return prime

# primes
prime(8, 32)
prime(256, 32)
prime(1024, 32)
