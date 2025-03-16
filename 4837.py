setA = [num for num in range(1, 13)]
subsetA = [[setA[j] for j in range(12) if i & (1 << j)] for i in range(1 << 12)]

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    cnt = 0

    for subset in subsetA:
        if len(subset) == N and sum(subset) == K:
            cnt += 1

    print(f'#{test_case} {cnt}')