import numpy as np


l1x = lambda a, b: abs(a[0] - b[0])
l1y = lambda a, b: abs(a[1] - b[1])
l2 = lambda a, b: np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def merge(points_y, l, m, r):
    i, j, aux = l, m, []
    while i < m or j < r:
        if i < m and j < r and points_y[i][1] > points_y[j][1]:
            aux.append(points_y[j])
            j += 1
        elif i < m:
            aux.append(points_y[i])
            i += 1
        else:
            aux.append(points_y[j])
            j += 1
    points_y[l:r] = aux

def search(points_x, points_y, l, r):
    if r - l < 2:
        return np.inf

    m = (l + r) // 2

    # search inside partitions
    delta1 = search(points_x, points_y, l, m)
    delta2 = search(points_x, points_y, m, r)
    delta = min(delta1, delta2)

    # sort points by y
    merge(points_y, l, m, r)

    # find the middle band in delta of x
    q = points[m]
    band = [p for p in points_y[l:r] if l1x(p, q) < delta]

    # search the middle band in delta of y
    for i in range(len(band)):
        p1 = band[i]
        for j in range(i + 1, len(band)):
            p2 = band[j]
            if l1y(p1, p2) < delta:
                delta = min(delta, l2(p1, p2))
            else:
                break

    # min distance
    return delta

def closest_pair(points):
    points = sorted(points)
    return search(points, points[:], 0, len(points))

points = [tuple(i) for i in np.random.rand(100, 2)]
points[:5]

closest_pair(points)
