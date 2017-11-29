from functools import reduce

# text
text = 'Premature optimization is the root of all evil -- DonaldKnuth'

# version 1
def longest_unique_sequence(sequence):
    i, j, k = 0, 0, set()
    bi, bj = 0, 0

    while j < len(sequence):
        if sequence[j] in k:
            k.remove(sequence[i])
            i += 1
        else:
            k.add(sequence[j])
            j += 1

        if j - i > bj - bi:
            bi, bj = i, j

    return bi, bj

i, j = longest_unique_sequence(text)
print(i, j, '"%s"' % text[i:j])

# version 2
def longest_unique_sequence(sequence):
    i, j = 0, 0
    bi, bj = 0, 0

    while j < len(sequence):
        if sequence[j] in sequence[i:j]:
            i += 1
        else:
            j += 1

        if j - i > bj - bi:
            bi, bj = i, j

    return bi, bj

i, j = longest_unique_sequence(text)
print(i, j, '"%s"' % text[i:j])

# version 3
def longest_unique_sequence(sequence):
    i, j = 0, 0
    b = 0, 0, 0

    while j < len(sequence):
        k = sequence[j] in sequence[i:j]
        i, j = i + k, j + 1 - k
        b = max(b, (j - i, i, j))

    return slice(b[1], b[2])

i = longest_unique_sequence(text)
print(i, '"%s"' % text[i])

# version 4
def longest_unique_sequence(sequence):
    i, b = 0, ''

    while i < len(sequence):
        if sequence[i] in sequence[:i]:
            i -= 1
            sequence = sequence[1:]
        else:
            i += 1
            b = max(b, sequence[:i], key=len)

    return b

longest_unique_sequence(text)

# version 5
def longest_unique_sequence(sequence):
    i, j = 0, 0

    while j < len(sequence):
        if sequence[j] in sequence[i:j]:
            i += 1
        else:
            j += 1
            yield sequence[i:j]

max(longest_unique_sequence(text), key=len)

# version 6
def longest_unique_sequence(sequence):
    i, k = 0, {}

    for j, x in enumerate(sequence):
        i = max(i, k.get(x, 0))
        k[x] = j + 1
        yield sequence[i:j + 1]

max(longest_unique_sequence(text), key=len)

# version 7
def longest_unique_sequence(sequence, best=''):
    for x in sequence:
        best = best[best.find(x) + 1:] + x
        yield best

max(longest_unique_sequence(text), key=len)
