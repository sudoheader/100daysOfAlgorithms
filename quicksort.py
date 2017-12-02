import numpy as np

# algorithm
def swap(data, i, j):
    data[i], data[j] = data[j], data[i]

def qsort3(data, left, right):
    # sorted
    if left >= right:
        return

    # select pivot
    i = np.random.randint(left, right + 1)
    swap(data, left, i)
    pivot = data[left]

    # i ~ pointes behind left partition
    # j ~ points ahead of right partition
    # k ~ current element
    i, j, k = left, right, left + 1

    # split to [left] + [pivot] + [right]
    while k <= j:
        if data[k] < pivot:
            swap(data, i, k)
            j -= 1
            k -= 1
        k += 1

    # recursion
    qsort3(data, left, i - 1)
    qsort3(data, j + 1, right)

def qsort(data):
    qsort3(data, 0, len(data) - 1)

# run
data = np.random.randint(0, 10, 100)
print(data)
qsort(data)
print(data)
