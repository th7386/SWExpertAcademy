def countdown(a):
    if a > 0:
        for i in range(1, a + 1):
            print(a)
            a -= 1
    else:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")


countdown(0)
countdown(10)