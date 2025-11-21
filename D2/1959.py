T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    total = -float('inf')
    if n <= m:
        short, long = n, m
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
    else:
        short, long = m, n
        B = list(map(int, input().split()))
        A = list(map(int, input().split()))
    for i in range(long - short + 1):
        temp = 0
        for j in range(short):
            temp += A[j] * B[i + j]
        if total <= temp:
            total = temp

    print(f"#{test_case} {total}")
