def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function


# 10 and 20 are the arguments.
result = calculator(lambda n1, n2: n1 * n2, 10, 20)
# The lambda multiplies them.
print(result)

print(calculator(lambda n1, n2: n1 + n2, 10, 20))

print("----Map----")
num_list = [0, 1, 2, 3, 4, 5]

double_list = map(lambda n: n * 2, num_list)

print(list(double_list))
print(list(double_list))

print("----Filter----")
numList = [30, 2, -15, 17, 9, 100]

greater_than_10 = filter(lambda n: n > 10, numList)
print(list(greater_than_10))
print(list(greater_than_10))
