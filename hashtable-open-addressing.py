import numpy as np
# algorithm
class HashTable:

    ratio_expand = .7
    ratio_shrink = .2
    min_size = 11
    empty = (None,)

    def __init__(self, size=None):
        self._size = size or self.min_size
        self._buckets = [None] * self._size
        self._count = 0

    def _entry(self, key):
        # get hash
        hash_ = hash(key)
        idx1 = None

        for i in range(self._size):
            # quadratic probing
            idx = (hash_ + i) % self._size
            entry = self._buckets[idx]

            # end of chain
            if not entry:
                break
            # remember first empty bucket
            elif entry is self.empty:
                if idx1 is None:
                    idx1 = idx
            # test key
            elif entry[0] == key:
                return idx, entry

        else:
            # out of space
            if idx1 is None:
                raise IndexError()

        # return first empty bucket
        return (idx, None) if idx1 is None else (idx1, None)

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
        entries = self._buckets
        self._buckets = [None] * self._size

        # store entries into new buckets
        for entry in entries:
            if entry and entry is not self.empty:
                idx, _ = self._entry(entry[0])
                self._buckets[idx] = entry

    def __len__(self):
        return self._count

    def __contains__(self, key):
        _, entry = self._entry(key)
        return bool(entry)

    def __getitem__(self, key):
        _, entry = self._entry(key)
        return entry and entry[1]

    def __setitem__(self, key, value):
        idx, entry = self._entry(key)

        # set value
        self._buckets[idx] = key, value

        # expand
        self._count += bool(not entry or entry is self.empty)
        self._ensure_capacity()

    def __delitem__(self, key):
        idx, entry = self._entry(key)

        # delete key and value
        if entry:
            self._buckets[idx] = self.empty

        # shrink
        self._count -= bool(entry and entry is not self.empty)
        self._ensure_capacity()

    def __iter__(self):
        for entry in self._buckets:
            if entry and entry is not self.empty:
                yield entry[0]

    def slots(self):
        return ''.join('-' if not p else 'o' if p is self.empty else 'x' for p in self._buckets)
# run
table = HashTable()

# add random values
for _ in range(1000):
    key, value = np.random.randint(1000), np.random.rand()
    if np.random.rand() >= .5:
        table[key] = value
    else:
        del table[key]

len(table), table._size
table.slots()

# print some values
for key in list(table)[:5]:
    print(key, table[key])

# delete all the values
for key in list(table):
    del table[key]

len(table), table._size
