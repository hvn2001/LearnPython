class ParentClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b


class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        self.c = c
        super().__init__(a, b)


obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)
