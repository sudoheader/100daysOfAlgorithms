def mccarthy91(n):
    k = 1
    while k:
        if n > 100:
              n -=10
              k -= 1
        else:
            n += 11
            k += 1
    return n

for i in range(70, 130, 10):
    print(i, mccarthy91(i))
    print(i + 1, mccarthy91(i + 1))
