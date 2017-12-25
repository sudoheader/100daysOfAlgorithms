import numpy as np
# algorithm
def hopfield_net(n):
    weights = np.zeros((n, n), dtype=int)

    def _store(data):
        nonlocal weights

        vector = np.array(data, dtype=int) * 2 - 1
        weights += np.outer(vector, vector) - np.eye(len(data), dtype=int)

    def _reconstruct(data):
        visible = np.array(data, dtype=int)

        while True:
            for i, v in np.ndenumerate(visible):
                visible[i] = weights[i] @ visible >= 0

            hidden = weights @ visible >= 0
            if np.all(hidden == visible):
                return visible

    return _store, _reconstruct

# run
store, reconstruct = hopfield_net(25)

# memories
store([
    1,0,0,0,1,
    0,1,0,1,0,
    0,0,1,0,0,
    0,1,0,1,0,
    1,0,0,0,1,
])

store([
    1,1,1,1,1,
    1,0,0,0,1,
    1,0,0,0,1,
    1,0,0,0,1,
    1,1,1,1,1,
])

store([
    0,0,1,0,0,
    0,0,1,0,0,
    1,1,1,1,1,
    0,0,1,0,0,
    0,0,1,0,0,
])

# reconstruction
reconstruct([
    1,1,1,1,1,
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,0,0,0,
]).reshape(5, 5)

reconstruct([
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,0,0,1,
    1,1,0,0,1,
]).reshape(5, 5)

reconstruct([
    1,0,0,0,0,
    0,1,0,0,0,
    0,0,1,0,0,
    0,0,0,1,0,
    0,0,0,0,1,
]).reshape(5, 5)

reconstruct([
    0,0,0,0,0,
    0,0,1,0,0,
    0,1,0,1,0,
    0,0,1,0,0,
    0,0,0,0,0,
]).reshape(5, 5)

reconstruct([
    0,0,1,0,0,
    0,0,1,0,0,
    0,0,1,0,0,
    0,0,1,0,0,
    0,0,1,0,0,
]).reshape(5, 5)
