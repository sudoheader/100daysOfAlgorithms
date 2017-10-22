def swap(x, y):
    s = x < y
    return x * s + y * (1 - s), y * s + x * (1 - s)

swap(3, 15), swap(15, 3)
swap(-13, 5), swap(5, -13)
