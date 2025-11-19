T = int(input())
for tc in range(1, T + 1):
    String = input()
    A = B = 1
    for x in String:
        if x == 'L':
            B += A
        else:
            A += B

    print("#{} {} {}".format(tc, A, B))
