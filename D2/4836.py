T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    red = []
    blue = []

    for i in range(N):
        purple = 0
        r1, c1, r2, c2, color = map(int, input().split())

        for y in range(c1, c2 + 1):
            for x in range(r1, r2 + 1):
                if color == 1:
                    red.append([x, y])
                else:
                    blue.append([x, y])

        for i in red:
            for j in blue:
                if i == j:
                    purple += 1
    print(f"#{test_case} {purple}")
