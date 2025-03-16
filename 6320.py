lst = ['가위', '바위', '보']
a = input()
b = input()
hong = ''
Lee = ''


def function(hong, Lee):
    if hong == lst[0] and Lee == lst[1]:
        print("바위가 이겼습니다!")
    elif hong == lst[1] and Lee == lst[2]:
        print("보가 이겼습니다!")
    elif hong == lst[2] and Lee == lst[0]:
        print("가위가 이겼습니다!")
    elif hong == lst[1] and Lee == lst[0]:
        print("바위가 이겼습니다!")
    elif hong == lst[0] and Lee == lst[2]:
        print("가위가 이겼습니다!")


hong = input()
Lee = input()
function(hong, Lee)