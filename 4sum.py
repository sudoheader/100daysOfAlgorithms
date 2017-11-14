import numpy as np
from itertools import combinations, product
from collections import defaultdict

# algorithm
def sum4(data):
    # store 2-sums
    sum_of_2 = defaultdict(list)
    for i, j in combinations(range(len(data)), 2):
        k = data[i] + data[j]
        sum_of_2[k].append((i, j))

        # match pairs of 2-sums
        sum_of_4 = set()
        for k in sum_of_2:
            if k >= 0 and -k in sum_of_2:
                for i, j in product(sum_of_2[k], sum_of_2[-k]):
                    index = tuple(sorted(set(i + j)))
                    if len(index) == 4:
                        sum_of_4.add(index)

        return sum_of_4

# run
n = 10
data = np.random.randint(-n, n, n)
data

for index in sum4(data):
    print(index, data[list(index)])
