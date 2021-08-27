from cogs import *
from out import print_result
from scipy.integrate import dblquad
from scipy.optimize import fsolve
from numpy import iinfo
import numpy as np
from sys import float_info

n = 9
m = 9
phi_func = simpson
theta_func = gauss
tau = 1
#func = generate_function(tau)
func = lambda theta, phi: theta*theta + theta*phi + phi*phi
h = lambda x: x*x
g = lambda x: -x*x + 2

x1, x2 = fsolve(lambda x: h(x) - g(x), (-1000, 1000))
ans = integrate(func, phi_func, theta_func, (lambda x: x1, lambda x: x2), (h, g), n, m)

#print("Функция f(θ, φ) = θ^2 + θφ + φ^2, ограниченная кривыми θ^2 и -θ^2 + 2")
print("Функция f(θ, φ) = sh(θ - φ^2) * exp(θφ), ограниченная кривыми θ^2 и -θ^2 + 2")
print("Количество интервалов N(φ) = {:^2}".format(n))
print("Количество интервалов M(θ) = {:^2}".format(m))
print("Метод прохождения по φ - Гаусс")
print("Метод прохождения по θ - Симпсон")
print("Значение 𝜏 = {:^3}".format(tau))
print("Результат = {:^3}".format(ans))
answ = dblquad(func, -1, 1, lambda x: x*x, lambda x: -x*x + 2)
print(answ)
#print_result((n, m))