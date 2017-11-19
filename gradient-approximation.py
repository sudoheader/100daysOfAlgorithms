import numpy as np

# algorithm
def gradient(fun, x, delta=1e-4):
    x = np.asfarray(x)
    grad = np.zeros(x.shape, dtype=x.dtype)

    for i, t in np.ndenumerate(x):
        x[i] = t + delta
        grad[i] = fun(x)
        x[i] = t - delta
        grad[i] -= fun(x)
        x[i] = t

    return grad / (2 * delta)

# quadratic form
def function(x):
    return 3 * x**2 + 2 * x + 1

for x in [-1, 0, 1]:
    print('x=', x, 'grad=', gradient(function, [x]))

# transcendental function
def function(X):
    x, y, z = X
    return x * np.sin(z) + y * np.cos(z) + z * np.exp(x + y)

for x in [[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]]:
    print('x=', x, 'grad=', gradient(function, x))

# determinant
function = np.linalg.det

for x in [
    [[1, 2, 3], [2, 3, 1], [3, 1, 2]],
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    [[1, 1], [1, 1]],
]:
    print('x=')
    print(x)
    print('grad=')
    print(gradient(function, x))
