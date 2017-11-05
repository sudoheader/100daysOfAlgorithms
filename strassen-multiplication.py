import numpy as np
def strassen (A, B):
    k = A.shape[0] // 2
    if k == 0:
        return A * B

    A11, A12 = A[:k, :k], A[:k, k:]
    A21, A22 = A[k:, :k], A[k:, k:]
    B11, B12 = B[:k, :k], B[:k, k:]
    B21, B22 = B[k:, :k], B[k:, k:]

    T1 = strassen(A11 + A22, B11 + B22)
    T2 = strassen(A21 + A22, B11)
    T3 = strassen(A11, B12 - B22)
    T4 = strassen(A22, B21 - B11)
    T5 = strassen(A11 + A12, B22)
    T6 = strassen(A21 - A11, B11 + B12)
    T7 = strassen(A12 - A22, B21 + B22)

    C = np.zeros(A.shape, dtype=A.dtype)
    C[:k, :k] = T1 + T4 - T5 + T7
    C[:k, k:] = T3 + T5
    C[k:, :k] = T2 + T4
    C[k:, k:] = T1 - T2 + T3 + T6

    return C

X = np.random.randint(0, 10, (8, 8))
X

Y = np.random.randint(0, 10, (8, 8))
Y

strassen(X, Y)
