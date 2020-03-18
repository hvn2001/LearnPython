class Student:

    def __init__(self):
        self.__name = None
        self.__RollNumber = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, RollNumber):
        self.__RollNumber = RollNumber

    def getRollNumber(self):
        return self.__RollNumber

st = Student()
st.setName("AAA")
st.setRollNumber("VVV")
print(st.getName())
