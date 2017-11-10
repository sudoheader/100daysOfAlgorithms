import numpy as np

def kth(items, k, depth=1):
    if len(items) == 1:
        return items[0], depth

    # randomize on pivot
    pivot = np.random.choice(items)
    split = np.sum(items <= pivot)

    # search partition
    if k < split:
        return kth(items[items <= pivot], k, depth + 1)
    else:
        return kth(items[items > pivot], k - split, depth + 1)

items = np.arange(1000000)
np.random.shuffle(items)
kth(items, len(items) // 2)
kth(items, 0)
kth(items, len(items) - 1)
