T = map(int, input().split(','))
T_list = [i for i in T if i % 2 == 1]
print(*T_list, sep=', ')
