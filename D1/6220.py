T = int(input())
for test_case in range(1, T + 1):
    words = input()
    if words.islower():
        print("#%d %s 는 소문자 입니다." % (test_case, words))
    else:
        print("#%d %s 는 대문자 입니다." % (test_case, words))