class Person:
    def getGender(self):
        return "Unknown"


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"


M = Male()
F = Female()

print(M.getGender())
print(F.getGender())
