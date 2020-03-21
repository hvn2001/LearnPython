name = "Ned"


def func():
    name = "Stark"  # cannot access data outside its scope unless the data has been passed in as an argument.
    # print(name)


func()
print(name)  # The value of 'name' remains unchanged.
