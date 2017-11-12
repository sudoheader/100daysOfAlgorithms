from collections import defaultdict
def lcs(X, Y):
    # momoize longest subsequences
    table = defaultdict(lambda: 0)

    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i] == Y[j]:
                table[i, j] = table[i - 1, j - 1] + 1
            else:
                table[i, j] = max(table[i - 1, j], table[i, j - 1])

    # reconstruction
    sequence = ''
    i, j = len(X) - 1, len(Y) - 1

    while i >= 0 and j >= 0:
        if X[i] == Y[j]:
            sequence = X[i] + sequence
            i -= 1
            j -= 1
        elif table[i - 1, j] < table[i, j - 1]:
            j -= 1
        else:
            i -= 1

    # result
    return table[len(X) - 1, len(Y) - 1], sequence

    # run
    lcs('longest common sub/sequence', 'shortest unique sub-sequence')
