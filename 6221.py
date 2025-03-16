list = ["가위", "바위", "보"]

Man1=input()
Man2=input()

if Man1==list[0] and Man2==list[1]:
    print("Result : Man2 Win!")
elif Man1==list[1]and Man2==list[0]:
    print("Result : Man1 Win!")
elif Man1==list[2]and Man2==list[1]:
    print("Result : Man1 Win!")
elif Man1==list[1]and Man2==list[2]:
    print("Result : Man2 Win!")
elif Man1==list[0]and Man2==list[2]:
    print("Result : Man1 Win!")
elif Man1==list[2]and Man2==list[0]:
    print("Result : Man2 Win!")
else:
    print("Result : Draw")
