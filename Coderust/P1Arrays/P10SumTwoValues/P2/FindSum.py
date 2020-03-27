def find_sum_of_two(A, val):
    i = 0
    j = len(A) - 1

    while i < j:
        s = A[i] + A[j]
        if s == val:
            return True

        if s < val:
            i += 1
        else:
            j -= 1

    return False


v = [1, 3, 4, 5, 7, 14, 15]
test = [3, 20, 1, 2, 7]

for i in range(len(test)):
    output = find_sum_of_two(v, test[i])
    print("find_sum_of_two(v, " + str(test[i]) + ") = " + str(output))
