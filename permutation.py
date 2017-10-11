# Next permutation
def permute(values):
    n = len(values)

    # i: position of pivot
    for i in reversed(range(n - 1)):
        if values[i] < values[i + 1]:
            break
    else:
        # very last permutation
        values[:] = reversed(values[:])
        return values

    # j: position of the next candidate
    for j in reversed(range(i, n)):
        if values[i] < values[j]:
            # swap pivot and reverse the tail
            values[i], values[j] = values[j], values[i]
            values[i + 1:] = reversed(values[i + 1:])
            break

    return values

print(permute(list('FADE')))
