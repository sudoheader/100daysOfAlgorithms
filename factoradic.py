# algorithm
fac = lambda i, *j: i and fac(*divmod(i, len(j) + 1), *j) or j or (i,)
dec = lambda i, k = 0, *j: j and dec(i * len(j) + i + k, *j) or i

# run
for i in range(0, 11):
    f = fac(i ** 3)
    d = dec(*f)
    print(d, '<->', ' '.join(map(str, f)))

fac(6281)
dec(*(1, 1, 4, 1, 2, 2, 1, 0))
