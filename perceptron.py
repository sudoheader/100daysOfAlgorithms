import numpy as np

X = np.array([
    [0, 1, 1], [1, 0, 1], [1, 1, 1], [-1, 1, 1], [1, -1, 1]
])
Y = np.array([1, 1, 1, 0, 0])
W = np.zeros(3)

def perceptron(x, w):
    return (x @ w >= 0).astype(int)

def train(x, y, w):
    for i in range(len(x)):
        # evaluate perceptron
        h = perceptron(x[i, :], w)

        # misclassification
        if h != y[i]:
            # positive sample
            if y[i] == 1:
                w += x[i, :]
            # negative sample
            else:
                w -= x[i, :]

    # evaluate
    return perceptron(x, w)

for _ in range(5):
    h = train(X, Y, W)
    print('w=', W, 'acc=', np.mean(h == Y))
