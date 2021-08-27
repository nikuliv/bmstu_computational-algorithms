from newton import newton
from spline import spline


def main():
    tab = [[i, i**2] for i in range(11)]
    x = 0.5

    print('\n\nТаблица функции (y = x^2):')
    print("+{:11s}|{:11s}+".format('-', '-').replace(' ', '-'))
    print('|     X     |     Y     |')
    print("|{:11s}|{:11s}|".format('-', '-').replace(' ', '-'))

    for i in tab:
        print('|{:11d}|{:11d}|'.format(i[0], i[1]))
        print("|{:11s}|{:11s}|".format('-', '-').replace(' ', '-'))
    print('\nX =', x)

    print('Результат интерполяции кубическим сплайном: {:.6f}'.format(spline(tab, x)))
    print('Значение y(x): {:.3f}'.format(x ** 2))
    print('Результат интерполяции полиномом Ньютона 3-ей степени: {:.6f}'.format(newton(tab, 3, x)))


if __name__ == "__main__":
    main()