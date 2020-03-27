def binary_search(a, key):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = low + ((high - low) // 2)

        if a[mid] == key:
            return mid

        if key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


arr = [1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222]
inputs = [10, 49, 99, 110, 176]

for i in range(len(inputs)):
    print("binary_search(arr, " + str(inputs[i]) + ") = " + str(binary_search(arr, inputs[i])))
