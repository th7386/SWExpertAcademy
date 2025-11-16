for tc in range(int(input())):
    N = input()
    M = input()
    result = []
    for i in N:
        result.append(M.count(i))
    print("#{} {}".format(tc + 1, max(result)))
