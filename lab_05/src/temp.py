from cogs import generate_function
import numpy as np
from scipy.integrate import dblquad

tau = 1
#func = generate_function(tau)
func = lambda x, y: x*x + x*y + y*y
answ = dblquad(func, -1, 1, lambda x: x*x, lambda x: -x*x + 2)
print("Результат = {:^3}".format(answ[0]))

d = -1
c = 1

F = lambda t: (d - c) / 2 * 1/9*(5*func(t, (d + c)/2 + (d - c) / 2 * (-3/5)**0.5) + 8*func(t, (d + c) / 2)
                                       + 5*func(t, (d + c) / 2) + (d - c) / 2 * (3.5)**0.5)

foo = lambda a, b : (b - a) / 2 * 1/9*(5*F((b + a)/2 + (b - a) / 2 * (-3/5)**0.5) + 8*F((b + a) / 2)
                                       + 5*F((b + a) / 2) + (b - a) / 2 * (3.5)**0.5)

af = lambda x: -x*x + 2
bf = lambda x: x*x

x = 0

a = af(x)
b = bf(x)
#
# a = af(0)
# b = bf(0)

print(foo(a,b))
print(func(x, (d + c)/2 + (d - c) / 2 * (-3/5)**0.5))
print(func(x, (d + c) / 2))
print(func(x, (d + c) / 2) + (d - c) / 2 * (3.5)**0.5)


