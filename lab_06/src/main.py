from cogs import *


def main():
    table = [[1, 2, 3, 4, 5, 6],
             [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]]
    none_str = '{:^10}'.format('-')

    print('┌{:^10s}┬{:^10s}┬{:^10s}┬{:^10s}┬{:^10s}┬{:^10s}┬{:^10s}┐'.format('-', '-', '-', '-',
                                                                             '-', '-', '-').replace(' ', '-'))
    print('|{:^10s}|{:^10s}|{:^10s}|{:^10s}|{:^10s}|{:^10s}|{:^10s}|'.format('x', 'y', 'left', 'center',
                                                                             'Runge', 'align', 'second'))
    print('|{:^10s}┼{:^10s}┼{:^10s}┼{:^10s}┼{:^10s}┼{:^10s}┼{:^10s}|'.format('-', '-', '-', '-',
                                                                             '-', '-', '-').replace(' ', '-'))

    res = list()
    res.append(left_diff(table[1], table[0]))
    res.append(centre_diff(table[1], table[0]))
    res.append(second_Runge(table[1], table[0]))
    res.append(align_vars(table[1], table[0]))
    res.append(second_diff(table[1], table[0]))
    for i in range(len(table[0])):
        print('|', end='')
        print('{:^10.3f}|{:^10.3f}|'.format(table[0][i], table[1][i]), sep='', end='')
        for j in range(len(res)):
            print('{:^10.5f}'.format(res[j][i]) if res[j][i] else none_str,
                  sep='', end='|')
        if i != len(table[0]) - 1:
            print('\n|{:^10s}┼{:^10s}┼{:^10s}┼{:^10s}┼{:^10s}┼{:^10s}┼{:^10s}|'.format('-', '-', '-', '-',
                                                                                       '-', '-', '-').replace(' ', '-'))
    print('\n└{:^10s}┴{:^10s}┴{:^10s}┴{:^10s}┴{:^10s}┴{:^10s}┴{:^10s}┘'.format('-', '-', '-', '-',
                                                                               '-', '-', '-').replace(' ', '-'))


if __name__ == "__main__":
    main()
