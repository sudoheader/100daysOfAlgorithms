'''
Tower of Hanoi
'''

def hanoi(height, left='left', right='right', middle='middle'):
    '''Recursive function hanoi'''
    #1 [recursively] move N-1 disks from left to middle
    #2 move largest disk from left to right
    #3 [recursively] move N-1 disks from middle to right
    if height:
        hanoi(height - 1, left, middle, right)
        print(left, '=>', right)
        hanoi(height - 1, middle, right, left)

hanoi(1)
hanoi(2)
hanoi(3)
