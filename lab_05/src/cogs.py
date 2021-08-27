from math import sin, cos, exp
import numpy as np


def get_legandre_func(n):
    if n == 0:
        return lambda x: 1
    elif n == 1:
        return lambda x: x
    else:
        return lambda x: (2 * n - 1) / n * x * get_legandre_func(n - 1)(x) - (n - 1) / n * get_legandre_func(n - 2)(x)


def bisection_method(f, a, b):
    eps = np.finfo(float).eps
    if (f(a) * f(b) >= 0):
        return None
    c = a
    while ((b - a) >= eps):
        c = (a + b) / 2
        if (abs(f(c)) < eps):
            break
        if (f(c) * f(a) > 0):
            a = c
        else:
            b = c
    return c


def find_legandre_roots(n):
    roots = []
    roots_cnt = 0
    max_cnt = n // 2
    h = 1 / (n + 2)
    i = -1

    while (roots_cnt < max_cnt):
        cur_root = bisection_method(get_legandre_func(n), i, i + h)
        if (cur_root and not cur_root in roots):
            roots.append(cur_root)
            roots_cnt += 1

        i += h
        if i > 0:
            i = -1
            h /= 2

    result = roots[:]
    if n % 2 != 0:
        result.append(0)
    result.extend([-x for x in roots])
    result = sorted(result)
    return result


def linalg_solve(A, B):
    n = len(B)

    for i in range(n):
        for j in range(i + 1, n):
            coefficient = -(A[j][i] / A[i][i])
            for k in range(i, n):
                A[j][k] += coefficient * A[i][k]
            B[j] += coefficient * B[i]
    x = [0] * n
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            B[i] -= x[j] * A[i][j]
        x[i] = B[i] / A[i][i]
    return x


def leggauss(n):
    B = []
    for i in range(n):
        B.append(0 if i % 2 else 2 / (i + 1))

    roots = find_legandre_roots(n)

    A = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(roots[j] ** i)
        A.append(temp)
    coefficients = linalg_solve(A, B)
    return roots, coefficients


def gauss(func, af, bf, t, n):
    a = af(t)
    b = bf(t)
    roots, coefficients = leggauss(n)
    l = 0

    m1 = (b + a) / 2
    m2 = (b - a) / 2

    for i in range(n):
        l += coefficients[i] * func(m1 + m2 * roots[i])
    l = l * m2

    return l


def simpson(func, af, bf, t, n):
    a = af(t)
    b = bf(t)
    h = (b - a) / (n - 1)
    l = 0
    for i in range((n - 1) // 2):
        l += func(a) + 4 * func(a + h) + func(a + 2 * h)
        a += 2 * h
    l = l * h / 3

    return l


def generate_function(tau):
    sub_func = lambda theta, phi: 2 * cos(theta) / (1 - (sin(theta) * cos(phi)) ** 2)
    main_func = lambda theta, phi, tau: (4 / np.pi) * (1 - exp(-tau * sub_func(theta, phi))) * cos(theta) * sin(theta)
    return lambda theta, phi: main_func(theta, phi, tau)


def integrate(func, phi_func, theta_func, phi_limits, thtea_limits, n, m):
    theta_result = lambda phi: theta_func(lambda theta: func(theta, phi), thtea_limits[0], thtea_limits[1], phi, n)
    result = phi_func(theta_result, phi_limits[0], phi_limits[1], lambda x: 0, m)
    return result
