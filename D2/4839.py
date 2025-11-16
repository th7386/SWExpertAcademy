def binary_search(left, right, key, cnt):
    if left > right:
        return None
    else:
        middle = (left + right) // 2
    if key == middle:
        return cnt
    elif key < middle:
        return binary_search(left, middle, key, cnt + 1)
    else:
        return binary_search(middle, right, key, cnt + 1)

T = int(input())

for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    winner = 0
    if binary_search(1, P, Pa, 0) < binary_search(1, P, Pb, 0):
        winner = 'A'
    elif binary_search(1, P, Pa, 0) > binary_search(1, P, Pb, 0):
        winner = 'B'

    print(f"#{test_case} {winner}")