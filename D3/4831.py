T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))

    count, current = 0, 0

    while current + K < N:
        for step in range(K, 0, -1):
            if current + step in station:
                current += step
                count += 1
                break
        else:
            count = 0
            break

    print("#{0} {1}".format(test_case, count))