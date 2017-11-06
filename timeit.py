import numpy as np
import time
from time import perf_counter
from itertools import combinations

def timeit(fn, fargs, n_range, seconds=5):
    print(f'[timeit] {seconds} seconds per N')

    # timeit for N
    bench = []
    for n in n_range:
        args = fargs(n)
        calls = 0

        # benchmark
        timer = perf_counter()
        while perf_counter() - timer < seconds:
            fn(args)
            calls += 1
        timer = perf_counter() - timer

        # results
        bench.append([np.e, n, timer / calls])
        print(f'[N={n}] {calls / timer:.2f} calls/sec')

    # estimate complexity
    bench = np.log(bench)
    (alpha, beta), *_ = np.linalg.lstsq(bench[:, :2], bench[:, -1])
    print(f'estimated O({np.exp(alpha):.3} * N ^ {beta:.3f})')

# setup
def combinatorial_sort(data):
    data = data.copy()
    for i, j in combinations(range(len(data)), 2):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]
    return data

def get_array(n):
    return np.random.randint(0, n, n)

# built-in sorted
print("BUILT-IN SORTED\n")
start_time = time.time()
n_range = [100, 1000, 10000, 100000, 1000000]
timeit(sorted, get_array, n_range)
end_time = time.time()
duration = end_time - start_time
print("Duration: %s seconds\n" % duration)

# numpy sort
print("NUMPY SORT\n")
start_time = time.time()
n_range = [100, 1000, 10000, 100000, 1000000]
timeit(np.sort, get_array, n_range)
end_time = time.time()
duration = end_time - start_time
print("Duration: %s seconds\n" % duration)

# combinatorial sort
print("COMBINATORIAL SORT\n")
start_time = time.time()
n_range = [10, 50, 100, 500, 1000]
timeit(combinatorial_sort, get_array, n_range)
end_time = time.time()
duration = end_time - start_time
print("Duration: %s seconds\n" % duration)
