T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    sum = N
    numbers = set()
    while True:
        for n in str(N):
            numbers.add(n)
        if len(numbers) == 10:
            break
        N += sum
    print("#{} {}".format(tc, N))
