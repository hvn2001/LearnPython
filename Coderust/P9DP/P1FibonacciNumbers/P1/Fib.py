def get_fibonacci(n):
    if n == 0 or n == 1:
        return n

    return get_fibonacci(n - 1) + get_fibonacci(n - 2)


inputs = [1, 5, 7, 10]

for i in range(len(inputs)):
    print("get_fibonacci(" + str(inputs[i]) + ") = " + str(get_fibonacci(inputs[i])))
