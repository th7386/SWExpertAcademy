a = ''
for i in range(1, 200 + 1):
    if i % 7 == 0 and i % 5 != 0:
        a += str(i) + ','
print(a[:-1])