T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    c = list(map(int, input().split()))

    sorted_w = sorted(w, reverse=True)
    sorted_c = sorted(c, reverse=True)

    result = [0 for _ in range(M)]

    for i in range(N):
        for j in range(M):
            if sorted_w[i] <= sorted_c[j]:
                if not result[j]:
                    result[j] = (sorted_w[i])
                    break

    print("#{} {}".format(tc, sum(result)))
