from itertools import groupby

my_int = 13749547874394873104972349

while True:

    my_str = str(my_int)

    if '8' not in my_str:
        break

    my_str = my_str.strip('8')

    my_str = ''.join('8' if k == '8' else ''.join(g) for k, g in groupby(my_str))

    my_lst = [''.join(g) for k, g in groupby(my_str, lambda x: x == '8')]

    for i in range(0, len(my_lst)):
        if my_lst[i] == '8':
            if int(my_lst[i - 1]) >= int(my_lst[i + 1]):
                my_lst[i] = '+'
            else:
                my_lst[i] = '-'
        else:
            my_lst[i] = str(int(my_lst[i]))

    my_int = eval(''.join(my_lst))

print(abs(my_int))
