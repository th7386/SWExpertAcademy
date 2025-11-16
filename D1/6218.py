a = int(input())
for i in range(1, a + 1):
    if a % i == 0:
        print("%d(은)는 %d의 약수입니다." % (i, a))