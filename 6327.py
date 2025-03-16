a = input()
b = a.split(",")

def pow(b):
    print("square(%d) => %d" % (int(b[0]), int(b[0]) ** 2))
    print("square(%d) => %d" % (int(b[1]), int(b[1]) ** 2))

pow(b)