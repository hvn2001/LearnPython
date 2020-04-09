import numpy as np

print('----A. Arithmetic----')
arr = np.array([[1, 2], [3, 4]])
# Add 1 to element values
print(repr(arr + 1))
# Subtract element values by 1.2
print(repr(arr - 1.2))
# Double element values
print(repr(arr * 2))
# Halve element values
print(repr(arr / 2))
# Integer division (half)
print(repr(arr // 2))
# Square element values
print(repr(arr ** 2))
# Square root element values
print(repr(arr ** 0.5))

print('----converts Fahrenheit to Celsius----')


def f2c(temps):
    return (5 / 9) * (temps - 32)


fahrenheits = np.array([32, -4, 14, -40])
celsius = f2c(fahrenheits)
print('Celsius: {}'.format(repr(celsius)))

print('----B. Non-linear functions----')
arr = np.array([[1, 2], [3, 4]])
# Raised to power of e
print(repr(np.exp(arr)))
# Raised to power of 2
print(repr(np.exp2(arr)))

arr2 = np.array([[1, 10], [np.e, np.pi]])
# Natural logarithm
print(repr(np.log(arr2)))
# Base 10 logarithm
print(repr(np.log10(arr2)))

print('----np.power----')
arr = np.array([[1, 2], [3, 4]])
# Raise 3 to power of each number in arr
print(repr(np.power(3, arr)))
arr2 = np.array([[10.2, 4], [3, 5]])
# Raise arr2 to power of each number in arr
print(repr(np.power(arr2, arr)))

print('----C. Matrix multiplication----')
arr1 = np.array([1, 2, 3])
arr2 = np.array([-3, 0, 10])
print(np.matmul(arr1, arr2))

arr3 = np.array([[1, 2], [3, 4], [5, 6]])
arr4 = np.array([[-1, 0, 1], [3, 2, -4]])
print(repr(np.matmul(arr3, arr4)))
print(repr(np.matmul(arr4, arr3)))
# This will result in ValueError
# print(repr(np.matmul(arr3, arr3)))


print('----Ex----')
arr = np.array([[-0.5, 0.8, -0.1], [0.0, -1.2, 1.3]])
arr2 = np.array([[1.2, 3.1], [1.2, 0.3], [1.5, 2.2]])
multiplied = arr * np.pi
added = arr + multiplied
squared = added ** 2

exponential = np.exp(squared)
logged = np.log(arr2)

matmul1 = np.matmul(logged, exponential)
matmul2 = np.matmul(exponential, logged)
