import datetime

name = input()
age = int(input())
P_age = datetime.datetime.now().year - 6 + (100 - age)

print("%s(은)는 %d년에 100세가 될 것입니다." % (name, P_age))
