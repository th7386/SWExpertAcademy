class Rectangle:
    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    def area(self):
        return self.width * self.length


ar = Rectangle(5, 4)
print("사각형의 면적: %d" % ar.area())
