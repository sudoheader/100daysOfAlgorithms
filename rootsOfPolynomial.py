import numpy as np

def roots(*coeffs):
    matrix = np.eye(len(coeffs) - 1, k=-1)
    matrix[:,-1] = np.array(coeffs[:0:-1]) / -coeffs[0]
    return np.linalg.eigvals(matrix)

# 10x - 1 = 0
roots(10, -1)

# x^2 - 2x + 1 = 0
roots(1, -2, 1)

# 2x^2 - 18 = 0
roots(2, 0, -18)

# x^5 + x^4 + x^3 + x^2 + x + 1 = 0
roots(1, 1, 1, 1, 1, 1)
