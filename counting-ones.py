import numpy as np
from collections import defaultdict
from itertools import count

# algorithm
def stream_counter():
    bucket = defaultdict(list)
    timestamp = count(1)
    estimate = None

    while True:
        code = yield estimate
        estimate = None

        # update buckets
        if code is True:
            bucket[1].append(next(timestamp))

            i = 1
            while len (bucket[i]) == 3:
                bucket[2 * i].append(bucket[i][1])
                del bucket[i][:2]
                i *= 2

        elif code is False:
            next(timestamp)

        # estimate count
        elif isinstance(code, int):
            counts = [i for i in bucket for t in bucket[i] if code < t] or [0]
            estimate = sum(counts) - counts[-1] // 2

            # debug
        elif code == 'debug':
            for i in bucket:
                print(i, bucket[i])

# run
n = 10 ** 6
ctr = stream_counter()
next(ctr)
for i in range(n):
    ctr.send(np.random.rand() >= .5)

for i in np.linspace(.99, 0, 5):
    k = int(i * n)
    print(f'last {n - k} bits: {ctr.send(k)}')

ctr.send('debug')
