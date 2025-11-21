t = [1] * 31
w = 2
while (w < 31):
    if w >= 3:
        t[w] = t[w - 1] + 2 * t[w - 2] + t[w - 3]
    else:
        t[w] = t[w - 1] + 2 * t[w - 2]
    w += 1
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f"#{tc} {t[N]}")
