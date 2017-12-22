# algorithm
class Unify:

    def __init__(self):
        self.reference = {}   # variable bindings
        self.checkpoint = []  # unification checkpoints
        self.var_ctx = 0      # unique variable id

    def variable(self, *args):
        self.var_ctx += 1
        return ['%s_%d' % (var, self.var_ctx) for var in args]

    def __call__(self, var_x, var_y):
        # resolve variable X
        while isinstance(var_x, str) and var_x in self.reference:
            var_x = self.reference[var_x]

        # resolve variable Y
        while isinstance(var_y, str) and var_y in self.reference:
            var_y = self.reference[var_y]

        # unified to self?
        if isinstance(var_x, str) and isinstance(var_y, str):
            if var_x == var_y:
                return True

        # unify free variable X
        if isinstance(var_x, str):
            self.reference[var_x] = var_y
            self.checkpoint[-1].append(var_x)
            return True

        # unify free variable Y
        if isinstance(var_y, str):
            self.reference[var_y] = var_x
            self.checkpoint[-1].append(var_y)
            return True

        # tuple is unified element-wise
        if isinstance(var_x, tuple) and isinstance(var_y, tuple):
            if len(var_x) == len(var_y):
                return all(self(i, j) for i, j in zip(var_x, var_y))

        # atom is unified on equality
        if isinstance(var_x, int) and isinstance(var_y, int):
            if var_x == var_y:
                return True

        # not unifiable
        raise KeyError()

    def __getitem__(self, var):
        # resolve tuple by members
        if isinstance(var, tuple):
            return tuple(self[i] for i in var)

        # resolve variable recursively
        if isinstance(var, str):
            if var in self.reference:
                return self[self.reference[var]]
            return var

        # atomic value
        if isinstance(var, int):
            return var

        # invalid object
        raise TypeError()

    def __enter__(self):
        # store unification checkpoint
        self.checkpoint.append([])

    def __exit__(self, exc_type, *args):
        # remove checkpoint and unbind variables
        for var in self.checkpoint.pop():
            if var in self.reference:
                del self.reference[var]

        # suppress exception
        if exc_type is not GeneratorExit:
            return True

def conc(PREFIX, SUFFIX, RESULT):
    HEAD, TAIL, CONC = unify.variable('HEAD', 'TAIL', 'CONC')

    with unify:
        unify(PREFIX, EMPTY) and unify(SUFFIX, RESULT)
        yield

    with unify:
        unify(PREFIX, (HEAD, TAIL)) and unify(RESULT, (HEAD, CONC))
        yield from conc(TAIL, SUFFIX, CONC)

# run
unify = Unify()
EMPTY = tuple()
prefix = (1, (2, EMPTY))
suffix = (3, (4, EMPTY))
result = (1, (2, (3, (4, EMPTY))))

# concatenate PREFIX and SUFFIX
for _ in conc(prefix, suffix, 'RESULT'):
    print(unify['RESULT'])

# what was concatenated to PREFIX if RESULT is this?
for _ in conc(prefix, 'SUFFIX', result):
    print(unify['SUFFIX'])

# this is super cool! if RESULT is this, what was PREFIX and SUFFIX?
for _ in conc('PREFIX', 'SUFFIX', result):
    print('possible answer is', unify['PREFIX'], 'and', unify['SUFFIX'])

# if PREFIX and SUFFIX are concatenated, would this be RESULT?
for _ in conc(prefix, suffix, result):
    print('yes')
    break
else:
    print('no')

for _ in conc(prefix, suffix, result):
    print('yes')
    break
else:
    print('no')

# most people won't solve this one
for _ in zip(range(5), conc('PREFIX', 'SUFFIX', 'RESULT')):
    print('PREFIX =', unify['PREFIX'])
    print('SUFFIX =', unify['SUFFIX'])
    print('RESULT =', unify['RESULT'])
    print()
