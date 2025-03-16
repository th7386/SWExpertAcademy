def mul_calc(*num):
    total = 1
    for i in num:
        if type(i) == str:
            print('에러발생')
            return
        total = total * i
    print(total)


mul_calc(1, 2, '4', 3)
