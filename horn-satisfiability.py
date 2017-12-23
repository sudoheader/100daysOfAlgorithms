from collections import defaultdict, deque
# algorithm
def knowledge_base(formulas):
    rules, variable, dependency = [], defaultdict(bool), defaultdict(list)

    def _clause(formula):
        # A, B, C => P
        neg, pos = formula.replace(' ', '').split('=>')
        neg, pos = set(neg.split('&')) - {''}, pos or None

        # add rule
        rules.append((neg, pos))

        # set variable and track dependencies
        for i in neg:
            dependency[i].append((neg, pos))

    # parse formulas and build knowledge base
    deque((_clause(i) for i in formulas.split('\n') if i), 0)

    return rules, variable, dependency

def resolution(rules, variable, dependency):
    # initial variables that have to be satisfied
    to_satisfy = [(neg, pos) for neg, pos in rules if not neg]

    while to_satisfy:
        neg, pos = to_satisfy.pop()

        # contradiction: true => false
        if not pos:
            return False

        # satisfy variable
        variable[pos] = True

        # update dependent rules
        for d_neg, d_pos in dependency[pos]:
            d_neg.remove(pos)

            # next variable to be satisfied
            if not d_neg and d_pos not in variable:
                to_satisfy.append((d_neg, d_pos))

    return True

def hornsat(formulas):
    rules, variable, dependency = knowledge_base(formulas)
    satisfiable = resolution(rules, variable, dependency)

    print(['CONTRADICTION', 'SATISFIABLE'][satisfiable])
    print(', '.join('%s=%s' % i for i in variable.items()))

# run
hornsat("""
X => Y
Y => Z
=> X
""")

hornsat("""
X => Y
Y => X
=> X
Y =>
""")

hornsat("""
P & Q & R & S => X
P & Q => R
R => S
X =>
=> P
=> R
""")

hornsat("""
P & Q & R & S => X
P & Q => R
R => S
X =>
=> P
=> Q
""")
