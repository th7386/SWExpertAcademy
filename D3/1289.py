T = int(input())
for tc in range(1, T + 1):
    num = input()
    differ = 0

    if num[0] == "1": differ += 1
    for i in range(1, len(num)):
        if num[i - 1] != num[i]:
            differ += 1
    print("#{} {}".format(tc, differ))
