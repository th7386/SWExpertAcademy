def subtree(root):
    global cnt
    cnt += 1

    for i in tree[int(root)]:
        if i:
            subtree(i)

    return cnt


for tc in range(int(input())):
    E, N = map(int, input().split())

    nodes = list(input().split())
    tree = [[] for _ in range(E + 2)]
    for t in range(0, len(nodes), 2):
        tree[int(nodes[t])].append(nodes[t + 1])
    cnt = 0

    print("#{} {}".format(tc + 1, subtree(N)))
