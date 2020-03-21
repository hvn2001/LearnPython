my_string = "This is MY string!"
print(my_string[0:4])
print(my_string[1:7])
print(my_string[8:len(my_string)])

print("----Slicing with a Step----")
print(my_string[0:7])  # A step of 1
print(my_string[0:7:2])  # A step of 2
print(my_string[0:7:5])  # A step of 5

print("----Reverse Slicing----")
my_string = "This is MY string!"
print(my_string[13:2:-1])  # rts YM si s
print(my_string[::-1])  # !gnirts YM si sihT
print(my_string[17:0:-2])

print("----Partial Slicing----")
my_string = "This is MY string!"
print(my_string[:8])  # All the characters before 'M'
print(my_string[8:])  # Al the characters starting from 'M'
print(my_string[:])  # The whole string
print(my_string[::-1])  # The whole string in reverse
