import numpy as np
# algorithm
def _power(x, y, identity=None, op=None):
    p = identity

    while y:
        p = op(p, x) if y & 1 else p
        x = op(x, x)
        y >>= 1

    return p

def power(x, y):
    return _power(x, y, identity=type(x)(1), op=type(x).__mul__)

def mod_power(x, y, n):
    return _power(x, y,
                  identity=1,
                  op=lambda a, b: (a * b) % n)

def matrix_power(x, y):
    return _power(x, y,
                  identity=np.eye(x.shape[0], dtype=x.dtype),
                  op=np.ndarray.__matmul__)

power(2, 100), 2 ** 100
power(2., 100), 2. ** 100
mod_power(2, 100, 1001), (2 ** 100) % 1001
matrix_power(np.array([[1, 1], [0, 1]]), 1000)
matrix_power(np.arange(9, dtype=float).reshape(3, 3), 100)
