from cogs import *


def main():
    tab = [[0.00, 1.0, -1.0],
           [0.15, 0.838771, -1.14944],
           [0.30, 0.655336, -1.29552],
           [0.45, 0.450447, -1.43497],
           [0.60, 0.225336, -1.56464],
           [0.75, -0.018310, -1.68164],
           [0.90, -0.278390, -1.78333],
           [1.05, -0.552430, -1.86742]]
    x = 0.5

    table_output(tab)

    print('\n\nx = 0.525:')
    print("+{:9s}|{:11s}|{:11s}|{:11s}|{:11s}+".format('-', '-', '-', '-', '-').replace(' ', '-'))
    print('|         |   n = 1   |   n = 2   |   n = 3   |   n = 4   | ')
    print("|{:9s}|{:11s}|{:11s}|{:11s}|{:11s}|".format('-', '-', '-', '-', '-').replace(' ', '-'))

    print('| Ньютон  |', end='')
    for i in range(1, 5):
        print('{:10.6f} |'.format(newton(tab, i + 1, x)), end='')
    print("\n|{:9s}|{:11s}|{:11s}|{:11s}|{:11s}|".format('-', '-', '-', '-', '-').replace(' ', '-'))
    print('| Эрмит   |', end='')
    for i in range(1, 5):
        print('{:10.6f} |'.format(hermite(tab, i + 1, x)), end='')
    print("\n|{:9s}|{:11s}|{:11s}|{:11s}|{:11s}|".format('-', '-', '-', '-', '-').replace(' ', '-'))

    root_tab = sorted(xy_swap(tab), key=lambda i: i[0], reverse=True)
    print('Корень функции:')
    print("+{:11s}|{:11s}|{:11s}|{:11s}+".format('-', '-', '-', '-', '-').replace(' ', '-'))
    print('|   n = 1   |   n = 2   |   n = 3   |   n = 4   |')
    print("|{:11s}|{:11s}|{:11s}|{:11s}|\n|".format('-', '-', '-', '-', '-').replace(' ', '-'), end='')
    for i in range(1, 5):
        print('{:10.6f} |'.format(newton(root_tab, i + 1, 0)), end='')
    print("\n|{:11s}|{:11s}|{:11s}|{:11s}|".format('-', '-', '-', '-', '-').replace(' ', '-'))


if __name__ == '__main__':
    main()
