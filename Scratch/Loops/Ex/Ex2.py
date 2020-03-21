def check_sum(num_list):
    for num1 in num_list:
        for num2 in num_list:
            if num1 + num2 == 0:
                return True
    return False


def check_sumSol(num_list):
    for first_num in range(len(num_list)):
        for second_num in range(first_num + 1, len(num_list)):
            if num_list[first_num] + num_list[second_num] == 0:
                return True
    return False


num_list = [10, -14, 26, 5, -3, 13, -5]
print(check_sumSol(num_list))
