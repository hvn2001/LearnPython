def removeEven(List):
    return [i for i in List if i % 2 == 1]


def removeEvenSol(List):
    # List comprehension to iter aover List and add to new list if not even
    return [number for number in List if number % 2 != 0]


print(removeEven([3, 2, 41, 3, 34]))
