a = input()
T_list = list(map(int, a.split(',')))
result = [[i * j for i in range(int(T_list[1]))] for j in range(int(T_list[0]))]
print(result)
