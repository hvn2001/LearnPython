def binary_search_rec(a, key, low, high):
    if low > high:
        return -1

    mid = low + ((high - low) // 2)
    if a[mid] == key:
        return mid
    elif key < a[mid]:
        return binary_search_rec(a, key, low, mid - 1)
    else:
        return binary_search_rec(a, key, mid + 1, high)


def binary_search(a, key):
    return binary_search_rec(a, key, 0, len(a) - 1)


arr = [1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222]
inputs = [10, 49, 99, 110, 176]

for i in range(len(inputs)):
    print("binary_search(arr, " + str(inputs[i]) + ") = " + str(binary_search(arr, inputs[i])))
