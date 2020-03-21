num_list = [10, 20, 30, 40]
print(num_list)


def multiply_by_10(myList):
    num_list[0] *= 10
    num_list[1] *= 10
    num_list[2] *= 10
    num_list[3] *= 10


multiply_by_10(num_list)
print(num_list)  # The contents of the list have been changed
# [100, 200, 300, 400]
