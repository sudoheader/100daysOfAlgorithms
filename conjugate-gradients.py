import numpy as np
def conjugate_gradients(A, b):
    x = np.zeros(A.shape[1])
    residuals = b - A @ x
    direction = residuals
    error = residuals.T @ residuals

    # step along conjugate directions
    while error > 1e-8:
        x += direction * error / (direction.T @ A @ direction)
        residuals = b - A @ x
        error1 = error
        error = residuals.T @ residuals
        direction = residuals + error / error1 * direction

    return x

A = np.random.rand(5, 3)
b = np.random.rand(5)

print('A')
print(A)
print('b')
print(b)
print('x')

# make system positive semidefinite
print(conjugate_gradients(A.T @ A, A.T @ b))
