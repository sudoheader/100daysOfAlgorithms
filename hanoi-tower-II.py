# algorithm
def get_rods(move, towers, left, middle, right):
    if towers:
        if (move << 1) & (1 << towers):
            right.append(towers)
            get_rods(move, towers - 1, middle, left, right)
        else:
            left.append(towers)
            get_rods(move, towers - 1, left, right, middle)

def get_move(towers, left, middle, right):
    if not towers:
        return 0
    if not left or right and left[0] < right[0]:
        move = 1 << (towers - 1)
        return move + get_move(towers - 1, middle, left, right[1:])
    else:
        return get_move(towers - 1, left[1:], right, middle)

def hanoi(towers):
    for i in range(2 ** towers):
        rods = [], [], []
        get_rods(i, towers, *rods)
        move = get_move(towers, *rods)
        print('{:2} moves -- {} {} {}'.format(move, *rods))

hanoi(2)
hanoi(3)
hanoi(4)
hanoi(5)
