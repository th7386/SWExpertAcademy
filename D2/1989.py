T = int(input())
for tc in range(1, T + 1):
    s = input()
    result = 0
    if s == s[::-1]:
        result = 1
    print("#{} {}".format(tc, result))
