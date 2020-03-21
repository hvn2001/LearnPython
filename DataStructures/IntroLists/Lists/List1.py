aList = [2, 'Educative', 'A']


def foo():
    print('Hello from foo()!')


anotherList = [aList, 'Python', foo, ['yet another list']]

print(anotherList[0])  # Elements of 'aList'
print(anotherList[0][1])  # Second element of 'aList'
print(anotherList[1])  # 'Python'
print(anotherList[3])  # 'yet another list'

# You can also invoke the functions inside a list!
anotherList[2]()  # 'Hello from foo()!'
