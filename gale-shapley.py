from collections import deque, defaultdict
# algorithm
def stable_match(men, women):
    free_men = deque(men)
    engaged = defaultdict(lambda: None)

    while free_men:
        i = free_men.popleft()

        # man proposes women according his preferences
        for j in men[i]:
            preference = women[j].index
            fiance = engaged[j]

            # woman accepts the better offer
            if not fiance or preference(i) < preference(fiance):
                engaged[j] = i
                fiance and free_men.append(fiance)
                break

    return [(m, w) for w, m in engaged.items()]

# run
men = {
    'adam': ['claire', 'diana'],
    'bob': ['diana', 'claire'],
}
women = {
    'claire': ['bob', 'adam'],
    'diana': ['adam', 'bob'],
}
stable_match(men, women)

men = {
    'adam': ['betty', 'claire', 'diana'],
    'bob': ['betty', 'claire', 'diana'],
    'charlie': ['betty', 'claire', 'diana'],
}
women = {
    'betty': ['charlie', 'bob', 'adam'],
    'claire': ['charlie', 'bob', 'adam'],
    'diana': ['charlie', 'bob', 'adam'],
}
stable_match(men, women)

men = {
    'adam': ['diana', 'alice', 'betty', 'claire'],
    'bob': ['betty', 'claire', 'alice', 'diana'],
    'charlie': ['betty', 'diana', 'claire', 'alice'],
    'david': ['claire', 'alice', 'diana', 'betty'],
}
women = {
    'alice': ['david', 'adam', 'charlie', 'bob'],
    'betty': ['adam', 'charlie', 'bob', 'david'],
    'claire': ['adam', 'bob', 'charlie', 'david'],
    'diana': ['david', 'adam', 'charlie', 'bob'],
}
stable_match(men, women)
