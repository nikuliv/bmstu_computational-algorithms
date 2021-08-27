from math import fabs, ceil

def point_selection(table, n, x, flag_tab=True):
    table_size = len(table)
    if flag_tab:
        closest_point_indx = min(range(table_size), key=lambda i: abs(table[i][0] - x))
    else:
        closest_point_indx = min(range(table_size), key=lambda i: abs(table[i] - x))
    req_space = ceil(n/2)

    if closest_point_indx + req_space + 1 > table_size:
        start = table_size - n
        end = table_size
    elif closest_point_indx < req_space:
        start = 0
        end = n
    else:
        start = closest_point_indx - req_space + 1
        end = start + n

    return start, end


def newton(orig_table, n, x):
    table = []
    for i in orig_table:
        table.append(i[:])

    start, end = point_selection(table, n, x)
    table = table[start:end]

    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            table[j][1] = (table[j][1] - table[j - 1][1]) / (table[j][0] - table[j - i][0])

    result = 0
    for i in range(n):
        temp = table[i][1]
        for j in range(i):
            temp *= (x - table[j][0])
        result += temp

    return result