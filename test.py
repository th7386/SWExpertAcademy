print("백슬래시\\")
print("작은 따옴포 \'를 출력합니다.")
print("큰 따옴포 \"를 출력합니다.")

# \n : 라인 피드(LF) - 줄바꿈 \t: 수평 탭(TAB) - 탭

# 's' 문자열 포맷
# 'c' 문자 포맷. 정수를 유니코드 문자로 변환해 출력
# 'd' 10진 정수로 출력
# 'o' 8진수로 출력
# 'x' 16진수로 출력
# 'f' 부동 소수점 숫자로 출력. 소수점 이하 6자리의 정밀도를 기본값으로 가짐
# '%' % 문자 자체를 출력

print("이름: %s" % "홍길동")
print("%c => %d" % (97, 97))
print("%d %o %x" % (10, 10, 10))
print("%f %d" % (3.14, 3.14))
print("%d 점은 상위 %d%%에 속합니다." % (98, 1))

print("이름: {0}, 나이: {1} 세".format("홍길동", 20))
print("{0:c} => {1}".format(97, 97))
print("{0} {1} {2:x}".format("가", ord("가"), ord("가")))
print("{0:.2f} {1:.2f}".format(3.14, 3.14))
print("이름: {name}, 나이: {age} 세".format(name="홍길동", age=20))
print("{0:<10}".format("좌측정렬"))
print("{0:>10}".format("우측정렬"))
print("{0:^10}".format("중앙정렬"))
print("{0:*^10}".format("중앙정렬"))
print("{0:0.2f}".format(3.141592))
print("{0:10.2f}".format(3.141592))
print("{0:010.2f}".format(3.141592))
print("{{ {0:.1f} }}".format(98.5))

a, b = 3, 2
print("{0} + {1} = {2}".format(a, b, a + b))

score = 80
if score >= 60:
    result = "합격입니다."
    print(result)

operand1, operator, operand2 = 0, "", 0

operand1 = int(input("첫 번째 숫자를 입력하세요: "))
operator = input("연산자를 입력하세요 (+, -, *, /): ")
operand2 = int(input("두 번째 숫자를 입력하세요: "))

if operator == "+":
    print("%d + %d = %d" % (operand1, operand2, operand1 + operand2))
elif operator == "-":
    print("%d - %d = %d" % (operand1, operand2, operand1 - operand2))
elif operator == "*":
    print("%d * %d = %d" % (operand1, operand2, operand1 * operand2))
elif operator == "/":
    print("%d / %d = %.2f" % (operand1, operand2, operand1 / operand2))
else:
   print("%s는 본 프로그램에서 지원하지 않는 연산자입니다." % operator)
