def count_of_1bits(value):
    n = 0
    while value:
        value &= value - 1
        n += 1
    return n

print(count_of_1bits(0b11001100))
