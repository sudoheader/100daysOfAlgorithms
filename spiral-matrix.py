from itertools import count

def spiral(n):
    matrix = [range(i * n + n)[-n:] for i in range(n)]
    X, C, R = {}, count(1), matrix

    while R:
        X.update(zip(R[0], C))
        R = list(zip(*[i[::-1] for i in R[1:]]))

    return [[X[j] for j in i] for i in matrix]

for i in spiral(3):
    print('\t'.join(map(str, i)))

for i in spiral(5):
    print('\t'.join(map(str, i)))
    
for i in spiral(7):
    print('\t'.join(map(str, i)))
