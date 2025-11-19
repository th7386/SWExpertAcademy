def func(n, m):
    if m == 0:
        return 1
    else:
        return n * func(n, m - 1)


for _ in range(10):
    TC = int(input())
    N, M = map(int, input().split())
    print("#" + str(TC), func(N, M))
