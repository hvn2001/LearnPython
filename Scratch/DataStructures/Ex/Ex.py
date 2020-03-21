my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]
my_tuple = (my_list[0], my_list[len(my_list) - 1], len(my_list))
print(my_tuple)

# ex2
test_list = [40, 35, 82, 14, 22, 66, 53]
k = 2
test_list.sort()
kth_min = test_list[len(test_list) - k]

# ex3
# num_list = [20, 9, 51, 81, 50, 42, 77]
num_list = [-10, 90, 15, 43]


def count_low_high(num_list):
    if len(num_list) == 0:
        return None
    high = len(list(filter(lambda num: num > 50 or num % 3 == 0, num_list)))
    low = len(list(filter(lambda num: num <= 50 and num % 3 != 0, num_list)))
    return [low, high]


print(count_low_high(num_list))
