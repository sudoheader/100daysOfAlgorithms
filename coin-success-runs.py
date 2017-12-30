import numpy as np
# algorithm
def probability(n, k, p, all_probs=False):
    F = np.zeros(n + 1)
    U = np.zeros(n + 1)
    R = p ** np.arange(k + 1)

    for i in range(k, n + 1):
        U[i] = R[k] - R[1:k] @ U[i-k+1:i][::-1]
        F[i] = U[i] - F[1:i] @ U[1:i][::-1]

    S = F.cumsum()

    return S if all_probs else S[-1]
# run
def print_chance(n):
    print(n, 'tosses; probability to see at least ...')
    for k in range(1, n + 1):
        p = probability(n, k, .5)
        print('%dx HEADS in row = %.4f' % (k, p))
        if p < 1e-4:
            break

print_chance(4)
print_chance(10)
print_chance(50)
print_chance(1000)
