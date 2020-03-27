def get_fibonacci(n):
    if n == 0 or n == 1:
        return n

    n_1 = 1
    n_2 = 0
    res = 0

    i = 2
    while i <= n:
        res = n_1 + n_2

        n_2 = n_1
        n_1 = res
        i += 1

    return res


inputs = [1, 5, 7, 10]

for i in range(len(inputs)):
    print("get_fibonacci(" + str(inputs[i]) + ") = " + str(get_fibonacci(inputs[i])))
