T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())
    Data = list(map(int, input().split()))
    for j in range(M):
        Data.append(Data.pop(0))
    print(f'#{i} {Data[0]}')
