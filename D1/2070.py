T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    if A == B:
        result = "="
    elif A > B:
        result = ">"
    else:
        result = "<"
    print("#{} {}".format(tc, result))
