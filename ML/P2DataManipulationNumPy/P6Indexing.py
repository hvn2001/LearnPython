import numpy as np

print('----A. Array accessing----')
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])
print(arr[4])

arr = np.array([[6, 3], [0, 2]])
# Subarray
print(repr(arr[0]))

print('----B. Slicing----')
arr = np.array([1, 2, 3, 4, 5])
print(repr(arr[:]))
print(repr(arr[1:]))
print(repr(arr[2:4]))
print(repr(arr[:-1]))
print(repr(arr[-2:]))

print('----B. multi-dimensional----')
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(repr(arr[:]))
print(repr(arr[1:]))
print(repr(arr[:, -1]))
print(repr(arr[:, 1:]))
print(repr(arr[0:1, 1:]))
print(repr(arr[0, 1:]))

print('----C. Argmin and argmax----')
arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [-3, 9, 1]])
print(np.argmin(arr[0]))
print(np.argmax(arr[2]))
print(np.argmin(arr))

print('----C. axis----')
arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [-3, 9, 1]])
print(repr(np.argmin(arr, axis=0)))
print(repr(np.argmin(arr, axis=1)))
print(repr(np.argmax(arr, axis=-1)))

print('----Ex: ----')


def direct_index(data):
    elem = data[1][2]
    return elem


def slice_data(data):
    slice1 = data[:, 1:]
    slice2 = data[0:3, :-2]
    return slice1, slice2


def argmin_data(data):
    argmin_all = np.argmin(data)
    argmin1 = np.argmin(data, axis=1)
    return argmin_all, argmin1


def argmax_data(data):
    argmax_neg1 = np.argmax(data, axis=-1)
    return argmax_neg1
