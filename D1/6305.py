a = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
b = []
a_list = [b.append(i) for i in a if i not in b]
print(b)
