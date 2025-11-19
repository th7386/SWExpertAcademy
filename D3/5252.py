T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A_dict = [input() for _ in range(N)]
    B_dict = [input() for _ in range(M)]

    tmp = []
    count = 0

    for i in range(len(A_dict)):
        for j in range(len(B_dict)):
            if A_dict[i] == B_dict[j] and B_dict[j] not in tmp:
                tmp.append(B_dict)
                count += 1

    print("#{} {}".format(tc, count))
