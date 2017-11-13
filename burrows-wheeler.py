# algorithm
def bwt(source):
    aux = [source[i:] + source[:i] for i in range(len(source))]
    aux.sort()
    idx = aux.index(source)
    return ''.join(i[-1] for i in aux), idx

def ibwt(source, idx):
    n = len(source)
    aux = [''] * n
    for _ in range(n):
        aux = sorted([i + j for i, j in zip(source, aux)])
    return aux[idx]

# run
target, i = bwt('the theta, there and there, was her')
target, i

ibwt(target, i)
