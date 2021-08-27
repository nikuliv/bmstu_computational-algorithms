from random import uniform, randint
import matplotlib.pyplot as plt
from func import root_mean_square
from numpy import array


def print_func(table):
    table = array(table)
    dots = [[]]
    x = table[0][0]
    while x <= table[len(table) - 1][0]:
        dots[0].append(x)
        x += 0.1

    for i in (1, 2, 5, 7):
        dots.append(root_mean_square(table, i))

    funcs = ['p = 1', 'p = 2', 'p = 5', 'p = 7', 'Data']

    fig, ax = plt.subplots()

    style = ["solid", "dotted", "dashed", "-."]
    for i in range(1,5):
        ax.plot(dots[0], dots[i], linestyle=style[i - 1])

    ax.scatter([i[0] for i in table], [i[1] for i in table],
               c='black', linewidths=0.25)

    plt.legend(funcs, loc=1)
    plt.grid()

    plt.show()


def print_comparsion(table):
    table = array(table)
    dots = [[]]
    x = table[0][0]
    while x <= table[len(table) - 1][0]:
        dots[0].append(x)
        x += 0.1

    for i in range(1,3):
        dots.append(root_mean_square(table, i))

    for i in range(len(table)):
        table[i][2] = 1

    for i in range(1,3):
        dots.append(root_mean_square(table, i))

    funcs = ['p = 1 (различный вес точек)',
             'p = 2 (различный вес точек)',
             'p = 1 (одинаковый вес точек)',
             'p = 2 (одинаковый вес точек)']

    fig, ax = plt.subplots()
    style = ["solid", "dotted", "dashed", "--"]
    for i in range(1,5):
        ax.plot(dots[0], dots[i], linestyle=style[i - 1])

    ax.scatter([i[0] for i in table], [i[1] for i in table], c='black')

    plt.legend(funcs, loc=1)
    plt.grid()

    plt.show()


def main():
    #table = [[i, uniform(-10,10), randint(1,30)] for i in range(8)]
    table = [[i, uniform(-10, 10), 1] for i in range(8)]

    print('Таблица функции:\n')

    print("+{:3s}|{:5s}|{:5s}|{:3s}+".format('-', '-', '-', '-').replace(' ', '-'))
    print('| № |  X  |  Y  |Вес|')
    print("|{:3s}|{:5s}|{:5s}|{:3s}|".format('-', '-', '-', '-').replace(' ', '-'))
    for i in range(len(table)):
        print('|{:3d}|{:5d}|{:5.1f}|{:3d}|'.format(i + 1, table[i][0], table[i][1], table[i][2]))
        print("|{:3s}|{:5s}|{:5s}|{:3s}|".format('-', '-', '-', '-').replace(' ', '-'))

    print_func(table)
    print_comparsion(table)


if __name__ == "__main__":
    main()