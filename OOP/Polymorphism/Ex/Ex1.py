from abc import ABC


class Shape(ABC):
    xsname = "Shape"

    def getName(self):
        return self.xsname;


class XShape(Shape):
    # initializer
    def __init__(self, name):
        self.xsname = name

    def getName(self):  # overriden method
        return super().getName() + ", " + self.xsname
