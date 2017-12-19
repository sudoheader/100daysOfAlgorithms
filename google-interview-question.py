import numpy as np
# algorithm
def solve_question(trials):
    # range to search in
    probability_range = np.array([0., 1.])

    while True:
        # prob. to see car in 10 minutes
        probability_10min = probability_range.mean()

        # simulate three 10-minute intervals
        events = np.random.rand(trials, 3) < probability_10min
        events = np.sum(events, axis=1) > 0

        # prob. to see car in 30 minutes
        probability_30min = np.mean(events)
        if abs(probability_30min - .95) < 1e-4:
            return probability_10min

        # bisection
        i = 0 if probability_30min < .95 else 1
        probability_range[i] = probability_10min

# run
solve_question(10**6)
solve_question(10**6)
solve_question(10**6)
1 - pow(0.05, 1/3)
