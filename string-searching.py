def search(text, pattern):
    i, k = 0, len(pattern)
    table = {c: k - i for i, c in enumerate(pattern)}

    while True:
        print(f'search @ {i}')
        if text[i:i + k] == pattern:
            print(f'FOUND @ {i}')
        if i + k < len(text):
            i += table.get(text[i + k], k + 1)
        else:
            break

text = 'A parabolic (or paraboloid or paraboloidal) reflector (or dish or mirror)'
len(text)
search(text, 'reflector')
search(text, 'not to be found')
