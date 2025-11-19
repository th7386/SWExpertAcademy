a = []

for i in range(2, 10):
    b = []
    if i % 3 != 0 and i % 7 != 0:
        for j in range(1, 10):
            if j % 3 != 0 and j % 7 != 0:
                b.append(i * j)
            else:
                continue
    a.append(b)

print(a)
