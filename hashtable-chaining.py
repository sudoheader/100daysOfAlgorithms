from types import SimpleNamespace
import numpy as np

# algorithm
class HashTable:

    ratio_expand = .8
    ratio_shrink = .2
    min_size = 11

    def __init__(self, size=None):
        self._size = size or self.min_size
        self._buckets = [None] * self._size
        self._list = None
        self._count = 0

    def _entry(self, key):
        # get hash and index
        idx = hash(key) % self._size

        # find entry by key
        p, q = self._buckets[idx], None
        while p and p.key != key:
            p, q = p.next, p

        # index, entry, previous entry
        return idx, p, q

    def _ensure_capacity(self):
        fill = self._count / self._size

        # expand or shrink?
        if fill > self.ratio_expand:
            self._size = self._size * 2 + 1
        elif fill < self.ratio_shrink and self._size > self.min_size:
            self._size = (self._size - 1) // 2
        else:
            return

        # reallocate buckets
        self._buckets = [None] * self._size

        # store entries into new buckets
        p = self._list
        while p:
            idx = hash(p.key) % self._size
            p.next = self._buckets[idx]
            self._buckets[idx] = p
            p = p.entry_next

    def __len__(self):
        return self._count

    def __contains__(self, key):
        _, p, _ = self._entry(key)
        return bool(p)

    def __getitem__(self, key):
        _, p, _ = self._entry(key)
        return p and p.value

    def __setitem__(self, key, value):
        idx, p, _ = self._entry(key)

        # set entry if key was found
        if p:
            p.value = value
            return

        # create new entry
        p = SimpleNamespace(
            key=key,
            value=value,
            next=self._buckets[idx],
            entry_next=self._list,
            entry_prev=None
        )

        # store to bucket
        self._buckets[idx] = p

        # store to list
        if self._list:
            self._list.entry_prev = p
        self._list = p

        # expand
        self._count += 1
        self._ensure_capacity()

    def __delitem__(self, key):
        idx, p, q = self._entry(key)

        # key not found
        if not p:
            return

        # remove from bucket
        if q:
            q.next = p.next
        else:
            self._buckets[idx] = p.next

        # remove from list
        if p.entry_next:
            p.entry_next.entry_prev = p.entry_prev
        if p.entry_prev:
            p.entry_prev.entry_next = p.entry_next
        else:
            self._list = p.entry_next

        # shrink
        self._count -= 1
        self._ensure_capacity()

    def __iter__(self):
        p = self._list
        while p:
            yield p.key
            p = p.entry_next

    def slots(self):
        return ''.join(p and 'x' or '-' for p in self._buckets)

# run
table = HashTable()
# add random values
for _ in range(1000):
    key, value = np.random.randint(1000), np.random.rand()
    table[key] = value

len(table), table._size
table.slots()

# print some values
for key in list(table)[:5]:
    print(key, table[key])

# delete all the values
for key in list(table):
    del table[key]

len(table), table._size
