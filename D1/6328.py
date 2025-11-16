a = input()
b = a.split(", ")


def fuction(b):
    if len(b[0]) > len(b[1]):
        print(b[0])
    else:
        print(b[1])


fuction(b)