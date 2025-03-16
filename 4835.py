T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    mn = N * 10000
    mx = 0

    for i in range(N - M + 1):
        sum = 0
        for j in range(i, i + M):
            sum += arr[j]
        if mn > sum:
            mn = sum
        if mx < sum:
            mx = sum

    print(f"#{test_case} {mx - mn}")

# 문제를 잘 읽자