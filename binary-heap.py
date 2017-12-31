# algorithm
identity = lambda i: i
def heapify(heap, key=identity):
    n = len(heap)
    for i in reversed(range(n // 2)):
        sift_down(heap, i, n, key=key)

def heap_push(heap, value, key=identity):
    i = len(heap)
    heap.append(value)
    sift_up(heap, i, key=key)

def heap_pop(heap, key=identity):
    item, heap[0] = heap[0], heap[-1]
    del heap[-1]
    heap and sift_down(heap, 0, len(heap), key=key)
    return item

def sift_down(heap, i, n, key=identity):
    # item to be sifted
    item = heap[i]
    item_key = key(item)

    while True:
        smallest, k = item_key, i
        j = 2 * i + 1

        # left child
        if j < n:
            left_key = key(heap[j])
            if left_key < smallest:
                smallest, k = left_key, j

        # right child
        if j + 1 < n and key(heap[j + 1]) < smallest:
            k = j + 1

        # swap or finish
        if k != i:
            heap[i] = heap[k]
            i = k
        else:
            break

    heap[i] = item

def sift_up(heap, i, key=identity):
    # item to be sifted
    item = heap[i]
    item_key = key(item)

    while i:
        j = i // 2

        if item_key < key(heap[j]):
            heap[i] = heap[j]
            i = j
        else:
            break

    heap[i] = item

def heap_sort(data, key=identity):
    heapify(data, key=key)

    for i in reversed(range(len(data))):
        data[0], data[i] = data[i], data[0]
        sift_down(data, 0, i, key=key)

    data.reverse()

# run
# priority queues
data1, data2 = [9, 7, 5, 3, 1], [8, 6, 4, 2, 0]

heapify(data1)
heapify(data2)

while data1 or data2:
    data2 and heap_push(data1, heap_pop(data2))
    print(heap_pop(data1), end=', ')

# string array
data = ['hello', 'bye', 'good-bye', 'hi', 'hey!', 'good night']

heap_sort(data)
data

heap_sort(data, key=len)
data

# string array treated as hexadecimal values
data = ['ff', '100', 'ac', '5', '99cc', '393', '000152']

heap_sort(data)
data

heap_sort(data, key=lambda i: int(i, 16))
data
