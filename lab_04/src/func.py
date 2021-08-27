def coef_finder(matrix, n):
    coefficients = []
    for i in range(n):
        summ = matrix[i][n]
        for j in range(len(coefficients)):
            summ -= coefficients[j] * matrix[i][j]
        coefficients.append(summ)
    return coefficients


def root_mean_square(table, n):
    n += 1
    matrix = [[0] * (n + 1) for i in range(n)]

    for i in range(n):
        for j in range(i, n):
            summ = 0
            for k in range(len(table)):
                summ += table[k][2] * table[k][0] ** (i + j)
            matrix[i][j] = matrix[j][i] = summ

        summ = 0
        for k in range(len(table)):
            summ += table[k][2] * table[k][1] * table[k][0] ** i
        matrix[i][n] = summ

    for i in range(n - 1, 0, -1):
        tmp = matrix[i][i]
        for j in range(n + 1):
            matrix[i][j] /= tmp

        for j in range(i):
            tmp = matrix[j][i]
            for k in range(n + 1):
                matrix[j][k] -= matrix[i][k] * tmp
    matrix[0][n] /= matrix[0][0]

    coefficients = coef_finder(matrix, n)

    dots = []
    x = table[0][0]
    while x <= table[len(table) - 1][0]:
        y = 0
        for j in range(len(coefficients)):
            y += coefficients[j] * x ** j
        dots.append(y)
        x += 0.1

    return dots