t = int(input())

for tc in range(1, t + 1):
    data = list(map(int, input().split()))
    for i in range(len(data)):
        if data[i] < 40:
            data[i] = 40

    sum_value = sum(data)
    avg_value = sum_value // 5

    print('#%d %d' % (tc, avg_value))
