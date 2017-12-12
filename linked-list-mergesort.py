from types import SimpleNamespace
from random import randint
# algorithm
def _merge(p, q):
    r, s = [Node()] * 2

    while p or q:
        if not q or p and p.value < q.value:
            r.next = p
            r, p = r.next, p.next
        else:
            r.next = q
            r, q = r.next, q.next

    return s.next

# recursive
def mergesort_recursive(head):
    # list is sorted
    if not (head and head.next):
        return head

    # make equal split
    p, q, r = head, head.next, None
    while q:
        p, q, r = p.next, q.next and q.next.next, p
    r.next = None

    # sort recursively
    p = mergesort_recursive(p)
    q = mergesort_recursive(head)

    # merge
    return _merge(p, q)

# iterative
def mergesort_iterative(head):
    splits = []

    while head:
        # sorted list of length 1
        head, p = head.next, head
        p.next = None
        splits.append((1, p))

        while len(splits) > 1:
            (i, p), (j, q) = splits[-2:]
            if i != j and head:
                break

            # merge
            splits[-2:] = [(i + j, _merge(p, q))]

    return splits and splits[0][1] or None

# utilities
Node = SimpleNamespace
def random_linked_list(size, r):
    head = None
    for i in range(size):
        head = Node(value=randint(0, r), next=head)
    return head

def print_list(head):
    def _iter(head):
        while head:
            yield head.value
            head = head.next

    print(list(_iter(head)))

# run
head = random_linked_list(size=20, r=10)
print_list(head)
for i in range(10):
    head = random_linked_list(size=3 * i, r=10)
    head = mergesort_recursive(head)
    print_list(head)
    
for i in range(10):
    head = random_linked_list(size=3 * i, r=10)
    head = mergesort_recursive(head)
    print_list(head)
