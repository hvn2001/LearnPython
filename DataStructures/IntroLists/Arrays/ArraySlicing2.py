import array

InitializerList = [2, 5, 43, 5, 10, 52, 29, 5]
NumberArray = array.array('i', InitializerList)

print(NumberArray[1:5])  # 2nd to 5th       -> array('i', [5, 43, 5, 10])
print(NumberArray[:-5])  # beginning to 3rd -> array('i', [2, 5, 43])
print(NumberArray[5:])  # 6th to end        -> array('i', [52, 29, 5])
print(NumberArray[:])  # beginning to end

print("------Changing or adding array elements--------")
integers = array.array('i', [1, 2, 3, 5, 7, 10])
print(integers)  # array('i', [1, 2, 3, 5, 7, 10])
# changing first element
integers[0] = 0
print(integers)  # array('i', [0, 2, 3, 5, 7, 10])

# changing 3rd to 5th element
integers[2:5] = array.array('i', [4, 6, 8])
print(integers)  # Output: array('i', [0, 2, 4, 6, 8, 10])

print("------add new items--------")
numbers = array.array('i', [1, 2, 3])

numbers.append(4)
print(numbers)  # array('i', [1, 2, 3, 4])

# extend() appends iterable to the end of the array
numbers.extend([5, 6, 7])
print(numbers)  # array('i', [1, 2, 3, 4, 5, 6, 7])

print("------concatenate --------")

odd = array.array('i', [1, 3, 5])
even = array.array('i', [2, 4, 6])

integers = array.array('i')  # creating empty array of integer
integers = odd + even

print(integers)

print("------del statement--------")

integerArray = array.array('i', [1, 2, 3, 3, 4])

del integerArray[2]  # removing third element
print(integerArray)  # Output: array('i', [1, 2, 3, 4])

del integerArray  # deleting entire array
# print(integerArray)  # Error: array is not defined


print("------remove/delete --------")

IntegerArray = array.array('i', [10, 11, 12, 12, 13])

IntegerArray.remove(12)
print(IntegerArray)  # array('i', [10, 11, 12, 13])

print(IntegerArray.pop(2))  # Output: 12
print(IntegerArray)  # array('i', [10, 11, 13])
