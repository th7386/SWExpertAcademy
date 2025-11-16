T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())
    A = set(input().split())
    B = set(input().split())

    print("#{} {}".format(i, len(A & B)))
