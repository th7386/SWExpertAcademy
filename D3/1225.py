T = 10
for _ in range(1, T + 1):
    tc = int(input())
    queue = list(map(int, input().split()))

    i = 1
    while True:
        if i > 5:
            i = 1
        t = queue.pop(0) - i
        if t <= 0:
            queue.append(0)
            break
        queue.append(t)
        i += 1
    print("#{} {} {} {} {} {} {} {} {}".format(tc, *queue))
