TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    income = list(map(int, input().split()))
    avg = sum(income) / N
    result = 0
    for i in income:
        if avg >= i:
            result += 1
    print("#{} {}".format(tc, result))
