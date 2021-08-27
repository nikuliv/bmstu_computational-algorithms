def one_side_diff(y1, y2, dx):
    return (y2 - y1) / dx


def left_diff(y, x):
    result = [None]
    for i in range(1, len(y)):
        result.append(one_side_diff(y[i - 1], y[i], x[i] - x[i - 1]))
    return result


def centre_diff(y, x):
    result = [None]
    for i in range(1, len(y) - 1):
        result.append(one_side_diff(y[i - 1], y[i + 1], x[i] - x[i - 1]) / 2)
    result.append(None)
    return result


def second_Runge(y, x):
    result = [None, None]
    for i in range(2, len(y)):
        result.append(one_side_diff(y[i - 1], y[i], x[i] - x[i - 1]) * 2
                      - one_side_diff(y[i - 2], y[i], 2 * (x[i] - x[i - 1])))
    return result


def align_vars_diff(y1, y2, x1, x2):
    return ((y1 - y2) / (y1 * y2)) / ((x1 - x2) / (x1 * x2))


def align_vars(y, x):
    result = list()
    for i in range(len(y) - 1):
        tmp = align_vars_diff(y[i], y[i + 1], x[i], x[i + 1])
        result.append(tmp * y[i] * y[i] / (x[i] * x[i]))
    result.append(None)
    return result


def second_diff_form(y1, y2, y3, dx):
    return (y1 - 2 * y2 + y3) / (dx * dx)


def second_diff(y, x):
    result = [None]
    for i in range(1, len(y) - 1):
        result.append(second_diff_form(y[i - 1], y[i], y[i + 1], x[i] - x[i - 1]))
    result.append(None)
    return result
