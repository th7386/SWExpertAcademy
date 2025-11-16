a = [1, 1]
b = [a.append(a[i - 1] + a[i]) for i in range(1, 9)]
print(a)