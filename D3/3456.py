T = int(input())
for tc in range(1, T + 1):
    a, b, c = map(int, input().split())
    result = 0
    if a == b:
        result = c
    elif a == c:
        result = b
    else:
        result = a
    print(f"#{tc} {result}")
