T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    print("#%d" % tc, end=' ')
    for i in range(n):
        print("%d/%d" % (1, n), end=' ')
    print()
