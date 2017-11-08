import numpy as np

def reservoir_sampling(size):
    i, sample = 0, []

    while True:
        item = yield i, sample

        i += 1
        k = np.random.randint(0, i)

        if len(sample) < size:
            sample.append(item)
        elif k < size:
            sample[k] = item
            
reservoir = reservoir_sampling(5)
next(reservoir)

for i in range(1000):
    k, sample = reservoir.send(i)
    if k % 100 == 0:
        print(k, sample)
