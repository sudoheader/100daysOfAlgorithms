import numpy as np
from collections import deque
from bitarray import bitarray
# algorithm
def ihash(x):
    h = 86813
    while True:
        for i in x:
            h = ((h + i) * 127733) % (1 << 32)
        yield h

def bloom_filter(array_bytes, k):
    array = bitarray(array_bytes * 8)
    array.setall(0)

    def _hash(x):
        for _, h in zip(range(k), ihash(x)):
            yield h % len(array)

    def _add(x):
        for h in _hash(x):
            array[h] = 1

    def _contains(x):
        return all(array[h] for h in _hash(x))

    return _add, _contains

def measure_accuracy(A, B, array_bytes, k):
    add, contains = bloom_filter(array_bytes, k)

    # store A
    deque((add(x) for x in A), 0)

    # find false positives in B
    fp = sum(contains(x) for x in B)

    # result
    acc = 1 - fp / len(B)
    print('{} hashes, {} false positives, {:.4f} accuracy'.format(k, fp, acc))

# run
n = 10 ** 6
A = set(map(tuple, np.random.randint(0, 256, (n, 4))))
B = set(map(tuple, np.random.randint(0, 256, (n, 4)))) - A
len(A), len(B)
for k in [1, 2, 3, 4]:
    measure_accuracy(A, B, n, k)
for k in [1, 2, 4, 6, 8]:
    measure_accuracy(A, B, n * 4, k)
