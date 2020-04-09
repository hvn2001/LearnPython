import numpy as np

print('----A. Summation----')

arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])
print(np.sum(arr))
print(repr(np.sum(arr, axis=0)))
print(repr(np.sum(arr, axis=1)))

print('----A.: np.cumsum----')
arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])
print(repr(np.cumsum(arr)))
print(repr(np.cumsum(arr, axis=0)))
print(repr(np.cumsum(arr, axis=1)))

print('----B. Concatenationn----')

arr1 = np.array([[0, 72, 3],
                 [1, 3, -60],
                 [-3, -2, 4]])
arr2 = np.array([[-15, 6, 1],
                 [8, 9, -4],
                 [5, -21, 18]])
print(repr(np.concatenate([arr1, arr2])))
print(repr(np.concatenate([arr1, arr2], axis=1)))
print(repr(np.concatenate([arr2, arr1], axis=1)))

print('----Ex: ----')


def get_sums(data):
    total_sum = np.sum(data)
    col_sum = np.sum(data, axis=0)
    return total_sum, col_sum


def get_cumsum(data):
    row_cumsum = np.cumsum(data, axis=1)
    return row_cumsum


def concat_arrays(data1, data2):
    col_concat = np.concatenate([data1, data2])
    row_concat = np.concatenate([data1, data2], axis=1)
    return col_concat, row_concat
