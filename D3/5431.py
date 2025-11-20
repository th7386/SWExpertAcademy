T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    result = []

    for i in range(1, N + 1):
        if i not in data:
            result.append(i)

    print(f'#{tc}', *result)
