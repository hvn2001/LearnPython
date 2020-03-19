class A:
    def __init__(self, x):
        self.x = x


class B(A):
    def __init__(self, x, y):
        self.y = y
        super().__init__(self, x)  # won’t compile


b = B(5, 6)
