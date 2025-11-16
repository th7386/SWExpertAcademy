T = int(input())
a = []
for i in range(1, T + 1):
    if T % i == 0:
        a.append(i)
print(a)
