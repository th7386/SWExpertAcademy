T = int(input())
for i in range(1, T + 1):
    N = int(input())
    myList = list(map(int, input().split()))

    print('#%d %d' % (i, max(myList) - min(myList)))
