import random

rand_num = random.random()
print(rand_num)

rand_num_in_range = random.uniform(30, 50)  # A random number between 30 and 50
print(rand_num_in_range)

str_list = ['a', 'b', 'c', 'd', 'e']
random.shuffle(str_list)  # Randomly shuffle a list
print(str_list)
