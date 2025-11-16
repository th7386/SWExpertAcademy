T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ai = list(map(str, input()))
    ai = list(map(int, ai))

    card = [0] * 10

    for i in ai:
        card[i] += 1
    idx = 0
    max = 0
    for i in range(10):
        if card[i] >= max:
            max = card[i]
            idx = i
    print("#%d %d %d" % (test_case, idx, max))
