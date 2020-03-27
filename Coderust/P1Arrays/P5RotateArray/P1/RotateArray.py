def reverse_array(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


def rotate_array(arr, n):
    length = len(arr)

    # Let's normalize rotations
    # if n > array size or n is negative.
    n = n % length
    if n < 0:
        # calculate the positive rotations needed.
        n = n + length
    # Let's partition the array based on rotations 'n'.
    # For example: 1, 2, 3, 4, 5 where n = 2.
    # -> 5, 4, 3, 2, 1
    # -> 4, 5, 3, 2, 1
    # -> 4, 5, 1, 2, 3

    reverse_array(arr, 0, length - 1)
    reverse_array(arr, 0, n - 1)
    reverse_array(arr, n, length - 1)


arr = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
print("Array Before Rotation")
print(arr)

rotate_array(arr, 2)
print("Array After Rotation")
print(arr)
