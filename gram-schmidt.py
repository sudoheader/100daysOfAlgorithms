import numpy as np
# algorithm
def gram_schmidt(X):
    O = np.zeros(X.shape)

    for i in range(X.shape[1]):
        # orthogonalization
        vector = X[:, i]
        space = O[:, :i]
        projection = vector @ space
        vector = vector - np.sum(projection * space, axis=1)

        # normalization
        norm = np.sqrt(vector @ vector)
        vector /= abs(norm) < 1e-8 and 1 or norm

        O[:, i] = vector

    return O
# run
# 6 column vectors in 4D
vectors = np.array([
    [1, 1, 2, 0, 1, 1],
    [0, 0, 0, 1, 2, 1],
    [1, 2, 3, 1, 3, 2],
    [1, 0, 1, 0, 1, 1]
], dtype=float)
# check orthogonality
vectors.T @ vectors
orthonormal = gram_schmidt(vectors)
orthonormal.round(5)
# check orthogonality
(orthonormal.T @ orthonormal).round(5)
# QR decomposition
matrix = np.array([
    [1, 1, -1],
    [1, 2, 1],
    [1, 3, 0]
], dtype=float)
Q = gram_schmidt(matrix)
Q.round(5)
R = Q.T @ matrix
R.round(5)
(Q @ R).round(5)
