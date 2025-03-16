a = int(input())


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if isPrime(a):
    print("소수입니다.")