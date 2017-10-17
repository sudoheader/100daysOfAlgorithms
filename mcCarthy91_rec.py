# stack limit is increased in this recursive version
def mccarthy91_rec(n):
    if n > 100:
        return n - 10
    else:
        return mccarthy91_rec(mccarthy91_rec(n + 11))

for i in range(70, 130, 10):
    print(i, mccarthy91_rec(i))
    print(i + 1, mccarthy91_rec(i + 1))
