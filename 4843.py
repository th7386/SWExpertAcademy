def special_sort(arr):
    s_arr = sorted(arr)
    length = len(s_arr)

    special_arr = []
    for i in range(length):
        if i % 2 == 0:
            special_arr.append(s_arr[length - 1 - i // 2])
        else:
            special_arr.append(s_arr[i // 2])
    return special_arr


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))

    print(f'#{test_case}', end=' ')
    for a in special_sort(ai)[:10]:
        print(a, end=' ')
    print()


# f(8) -> f(6) + f(5), f(6) -> f(4) + f(3) , f(5) -> f(3) + f(2) , f(4) -> f(2) + f(1)
#                       6         3       3    5          3      2   3           2      1