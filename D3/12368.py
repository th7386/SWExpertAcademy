T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    C = A + B
    answer = C % 24
    print("#{} {}".format(tc, answer))
