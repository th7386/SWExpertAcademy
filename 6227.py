a = ''
for i in range(100, 300 + 1):
    if (i // 100) % 2 == 0 and (i // 10) % 2 == 0 and i % 2 == 0:
        a += str(i) + ','
print(a[:-1])