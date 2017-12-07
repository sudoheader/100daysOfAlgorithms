# algorithm
def detect_cycle(head):
    if not head:
        return

    # cycle detection: 2k = k (mod C)
    p, q = head, head.next
    while q and p is not q:
        p, q = p.next, q.next and q.next.next

    if p is q:
        # cycle removal: k + T = 0 (mod C)
        p = head
        while p is not q.next:
            p, q = p.next, q.next

        # fix the last link
        q.next = None
        return q

# utilities
class Node:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __repr__(self):
        return str(self.__dict__)

def linked_list_with_cycle(length, cycle):
    head, tail = None, None

    for i in range(length):
        # prepend head
        head = Node(value=length - i, next=head)
        tail = tail or head

        # make cycle of length C
        if i + 1 == cycle:
            tail.next = head

    return head

# run
linked_list = linked_list_with_cycle(10, 4)
print(linked_list)
detect_cycle(linked_list)
linked_list = linked_list_with_cycle(5, 1)
detect_cycle(linked_list)
linked_list = linked_list_with_cycle(10, 5)
detect_cycle(linked_list)
linked_list = linked_list_with_cycle(25, 25)
detect_cycle(linked_list)
