student = {'홍길동': '010-1111-1111', '이순신': '010-1111-2222', '강감찬': '010-1111-3333'}


def function(name, dic):
    if name in dic:
        print("%s의 전화번호는 %s입니다." % (name, dic[name]))
    else:
        print("등록된 학생이 아닙니다.")


a = "아래 학생들의 전화번호를 조회할 수 있습니다.\n홍길동\n이순신\n강감찬\n전화번호를 조회하고자 하는 학생의 이름을 입력하십시오."
print(a)
T = input()
function(T, student)
