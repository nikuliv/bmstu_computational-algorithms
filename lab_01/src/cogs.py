from math import fabs, ceil


def table_output(table):
    print("+{:7s}|{:11s}|{:11s}+".format('-', '-', '-').replace(' ', '-'))
    for i in table:
        print('|{:^7.2f}|{:^11.6f}|{:^11.6f}|'.format(i[0], i[1], i[2]))
        print("|{:7s}|{:11s}|{:11s}|".format('-', '-', '-').replace(' ', '-'))


def point_selection(table, n, x):
    table_size = len(table)
    closest_point_indx = min(range(table_size), key=lambda i: fabs(table[i][0] - x))
    req_space = ceil(n/2)

    if closest_point_indx + req_space + 1 > table_size:
        start = table_size - n
        end = table_size
    elif closest_point_indx < req_space:
        start = 0
        end = n
    else:
        start = closest_point_indx - req_space
        end = start + n

    result = table[start:end]

    return result


def newton(orig_table, n, x):
    table = []
    for i in orig_table:
        table.append(i[:])

    table = point_selection(table, n, x)

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


def hermite(orig_table, n, x):
    table = []
    for i in orig_table:
        table.append(i[:])
        table.append(i[:])

    table = point_selection(table, n, x)

    for i in range(n - 1, 0, -1):
        if fabs(table[i][0] - table[i - 1][0]) < 1e-7:
            table[i][1] = table[i][2]
        else:
            table[i][1] = (table[i][1] - table[i - 1][1]) / (table[i][0] - table[i - 1][0])

    for i in range(2, n):
        for j in range(n - 1, i - 1, -1):
            table[j][1] = (table[j][1] - table[j - 1][1]) / (table[j][0] - table[j - i][0])

    result = 0
    for i in range(n):
        temp = table[i][1]
        for j in range(i):
            temp *= (x - table[j][0])
        result += temp

    return result


def xy_swap(table):
    new_tab = []
    for i in table:
        new_tab.append(i[:])
    for i in new_tab:
        i[0], i[1] = i[1], i[0]
    return new_tab
