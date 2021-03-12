from cogs import *


def main():
    tab = [[0, 1, 4, 9, 16],
           [1, 2, 5, 10, 17],
           [4, 5, 8, 13, 20],
           [9, 10, 13, 18, 25],
           [16, 17, 20, 25, 32]]
    x_list = [0, 1, 2, 3, 4]
    y_list = [0, 1, 2, 3, 4]
    x, y = 1.5, 1.5

    print('\n\nz(1.5, 1.5):')
    print("+{:9s}|{:11s}|{:11s}|{:11s}+".format('-', '-', '-', '-').replace(' ', '-'))
    print('| ny \\ nx |     1     |     2     |     3     |')
    print("|{:9s}|{:11s}|{:11s}|{:11s}|".format('-', '-', '-', '-').replace(' ', '-'))

    print('| z(x, y) |', end='')
    for i in range(1, 4):
        print('{:10.6f} |'.format(multivariate_interpolation(x_list, y_list, tab, x, y, i + 1, i + 1)), end='')
    print("\n|{:9s}|{:11s}|{:11s}|{:11s}|".format('-', '-', '-', '-').replace(' ', '-'))


if __name__ == '__main__':
    main()
