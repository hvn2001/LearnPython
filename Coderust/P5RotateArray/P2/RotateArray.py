def rotate_array(arr, n):
    length = len(arr)

    # Let's normalize rotations
    # if n > array size or n is negative.
    n = n % length
    if n < 0:
        # calculate the positive rotations needed.
        n = n + length

    temp = []
    # copy last N elements of array into temp
    for i in range(length - n, length):
        temp.append(arr[i])

    # shift original array
    for i in range(length - 1, n - 1, -1):
        arr[i] = arr[i - n];

    # copy temp into original array
    for i in range(n):
        arr[i] = temp[i]


arr = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
print("Array Before Rotation")
print(arr)

rotate_array(arr, -3)
print("Array After Rotation")
print(arr)
