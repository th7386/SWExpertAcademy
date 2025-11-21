def inorder(n):
    global value
    if n <= N:
        # 왼쪽 자식
        inorder(n * 2)
        tree[n] = value
        value += 1
        # 오른쪽 자식
        inorder((n * 2 + 1))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    value = 1

    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')
