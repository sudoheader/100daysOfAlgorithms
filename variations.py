from random import randrange
# algorithm
def ffact(n, k, _cache={}):
    if (n, k) not in _cache:
        f = 1
        for i in range(k):
            f *= n - i

        _cache[n, k] = f

    return _cache[n, k]

def variation_to_order(variation):
    alphabet = list('0123456789')
    n = len(variation)

    order = 1
    order -= ffact(9, n - 1)
    for i in range(1, n):
        order += ffact(10, i) - ffact(9, i - 1)

    for i in range(n):
        index = alphabet.index(variation[i])
        order += index * ffact(9 - i, n - i - 1)
        del alphabet[index]

    return order

def order_to_variation(order):
    for n in range(1, 11):
        k = ffact(10, n) - ffact(9, n - 1)
        if k >= order:
            break
        order -= k

    order -= (n != 1)
    alphabet = list('0123456789')
    variation = ''

    for i in range(n):
        k = ffact(9 - i, n - i - 1)
        index = order // k + (i == 0) - (n == 1)
        order %= k
        variation += alphabet[index]
        del alphabet[index]

    return variation

# run
variation_to_order('9876543210')

print(' variation    order')
for _ in range(10):
    i = randrange(8877691)
    variation = order_to_variation(i)
    order = variation_to_order(variation)
    assert i == order
    print('%10s ## %d' % (variation, order))
