a, b = map(int, input().split())
if a < b:
    if a == 1 and b == 1:
        print("A")
    print("B")
else:
    if a == 3 and b == 1:
        print("B")
    print("A")
