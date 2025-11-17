TC = int(input())
for tc in range(1, TC + 1):
    A, B = map(int, input().split())
    if A >= 10 or B >= 10:
        print("#{} {}".format(tc, -1))
    else:
        print("#{} {}".format(tc, A * B))
