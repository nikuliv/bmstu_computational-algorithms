def straight_walk(ksi, eta, length, table, h):
    for i in range(3, length):
        F = -3 * ((table[i - 1][1] - table[i - 2][1]) /
                  h[i - 1] - (table[i - 2][1] - table[i - 3][1]) / h[i - 2])
        denominator = -2 * (h[i - 1] + h[i - 2]) - h[i - 2] * ksi[i - 1]
        ksi[i] = h[i - 1] / denominator
        eta[i] = (F + h[i - 2] * eta[i - 1]) / denominator


def forward_walk(ksi, eta, c):
    c[-2] = eta[-1]
    for i in range(len(c) - 2, 1, -1):
        c[i] = ksi[i + 1] * c[i + 1] + eta[i + 1]


def find_additional(d, b, a, c, h):
    for i in range(1, len(d) - 1):
        d[i] = (c[i + 1] - c[i]) / 3 / h[i]
        b[i] = (a[i + 1] - a[i]) / h[i] - h[i] / 3 * (c[i + 1] + 2 * c[i])


def find_section(points: list, x):
    if points[0][0] - points[1][0] < 0:
        i = 0
        while x > points[i][0] and i < len(points) - 1:
            i += 1
        return i
    else:
        i = 0
        while x < points[i][0] and i < len(points) - 1:
            i += 1
        return i


def find_result(x, a, b, c, d, xl):
    return a + b * (x - xl) + c * (x - xl) ** 2 + d * (x - xl) ** 3


def spline(table, x):
    a = [0] + [p[1] for p in table]
    h = [0] + [table[i][0] - table[i - 1][0] for i in range(1, len(table))]
    c = [0 for i in range(len(a))]
    b = c[:]
    d = c[:]
    ksi = c[:]
    eta = c[:]
    straight_walk(ksi, eta, len(c), table, h)
    forward_walk(ksi, eta, c)
    find_additional(d, b, a, c, h)
    i = find_section(table, x)
    result = find_result(x, a[i], b[i], c[i], d[i], table[i - 1][0])
    return result