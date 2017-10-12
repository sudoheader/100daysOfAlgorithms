ops = {
    '+': float.__add__,
    '-': float.__sub__,
    '*': float.__mul__,
    '/': float.__truediv__,
    '^': float.__pow__,
}

def postfix(expression):
    stack = []

    for x in expression.split():
        if x in ops:
            x = ops[x](stack.pop(-2), stack.pop(-1))
        else:
            x = float(x)
        stack.append(x)

    return stack.pop()

postfix('1 2 + 4 3 - + 10 5 / *')
