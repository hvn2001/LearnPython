List = list(range(10))
print(List)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(List[0:4])  # 0, 1, 2, 3

print("------Stepped Indexing----------")
List = list(range(10))  # define a range of values 0
print(List[0:9])  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(List[0:10])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(List[0:])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(List[0:9:2])  # 0, 2, 4, 6, 8
print(List[9:0:-2])  # 9, 7, 5, 3, 1

print("------Initializing list elements----------")
x = list(range(5))
print(x)  # 0, 1, 2, 3, 4
x[1:4] = [45, 21, 83]
print(x)  # 0, 45, 21, 83, 4

print("------Deleting elements----------")
List = list(range(10))
print(List)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
del List[::2]
print(List)  # 1, 3, 5, 7, 9

print("------Negative Indexing----------")
List = list(range(10))
print(List)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(List[4:-1])  # 4, 5, 6, 7, 8

print("------Slicing Strings----------")
my_string = "somehow"
string1 = my_string[:4]
string2 = my_string[4:]
print(string1, string2)
