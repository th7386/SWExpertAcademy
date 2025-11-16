for tc in range(int(input())):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N + 1)]

    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value
    for i in range(N, 0, -1):
        if i // 2 > 0:
            tree[i // 2] += tree[i]
    print("#{} {}".format(tc + 1, tree[L]))
