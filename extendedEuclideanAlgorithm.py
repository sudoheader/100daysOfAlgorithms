def gcd(x, y):
    u0, v0 = 1, 0
    u1, v1 = 0, 1
    while y:
        q = x // y
        u0, u1 = u1, u0 - q * u1
        v0, v1 = v1, v0 - q * v1
        x, y = y, x % y
    return x, u0, v0

gcd(5, 7)
gcd(2*3*7*9*11, 6*12*13)
gcd(32423940, 230934894)
gcd(150, 100)
gcd(151, 100)
