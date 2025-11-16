class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.__length = length

    def area(self):
        return self.__length ** 2


Squ = Square(3)
print("정사각형의 면적: %d" % Squ.area())
