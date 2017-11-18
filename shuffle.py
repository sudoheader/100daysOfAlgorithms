import numpy as np
# algorithm
def shuffle(data):
    n = len(data)
    for i in range(n):
        k = np.random.randint(i, n)
        data[i], data[k] = data[k], data[i]

    return data

# shuffle
data = list(range(10))
shuffle(data)
shuffle(data)
shuffle(data)
