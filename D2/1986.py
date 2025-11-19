T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    if N % 2 == 0:
        result = -N // 2
    else:
        result = (N + 1) // 2
    print("#{} {}".format(tc, result))
