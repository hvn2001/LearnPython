import numpy as np

print('----A. Filtering data----')

arr = np.array([[0, 2, 3],
                [1, 3, -6],
                [-3, -2, 1]])
print(repr(arr == 3))
print(repr(arr > 0))
print(repr(arr != 1))
# Negated from the previous step
print(repr(~(arr != 1)))

print('----A. np.isnan----')
arr = np.array([[0, 2, np.nan],
                [1, np.nan, -6],
                [np.nan, -2, 1]])
print(repr(np.isnan(arr)))

print('----B. Filtering in NumPy----')
print(repr(np.where([True, False, True])))

arr = np.array([0, 3, 5, 3, 1])
print(repr(np.where(arr == 3)))

arr = np.array([[0, 2, 3],
                [1, 0, 0],
                [-3, 0, 0]])
x_ind, y_ind = np.where(arr != 0)
print(repr(x_ind))  # x indices of non-zero elements
print(repr(y_ind))  # y indices of non-zero elements
print(repr(arr[x_ind, y_ind]))

print('----B. np.where with 3 arguments----')
np_filter = np.array([[True, False], [False, True]])
positives = np.array([[1, 2], [3, 4]])
negatives = np.array([[-2, -5], [-1, -8]])
print(repr(np.where(np_filter, positives, negatives)))

np_filter = positives > 2
print(repr(np.where(np_filter, positives, negatives)))

np_filter = negatives > 0
print(repr(np.where(np_filter, positives, negatives)))

print('----B. broadcasting with np.where----')
np_filter = np.array([[True, False], [False, True]])
positives = np.array([[1, 2], [3, 4]])
print(repr(np.where(np_filter, positives, -1)))

print('----C. Axis-wise filtering----')
arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [3, 9, 1]])
print(repr(arr > 0))
print(np.any(arr > 0))
print(np.all(arr > 0))

print('----C. np.any and np.all with the axis----')
arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [3, 9, 1]])
print(repr(arr > 0))
print(repr(np.any(arr > 0, axis=0)))
print(repr(np.any(arr > 0, axis=1)))
print(repr(np.all(arr > 0, axis=1)))

print(
    '----C. images: np.any to obtain a boolean array representing the rows that have at least one positive number----')
arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [3, 9, 1]])
has_positive = np.any(arr > 0, axis=1)
print(has_positive)
print(repr(arr[np.where(has_positive)]))

print('----Ex: ----')


def get_positives(data):
    x_ind, y_ind = np.where(data > 0)
    return data[x_ind, y_ind]


def replace_zeros(data):
    zeros = np.zeros_like(data)
    zero_replace = np.where(data > 0, data, zeros)
    return zero_replace


def replace_neg_one(data):
    neg_one_replace = np.where(data > 0, data, -1)
    return neg_one_replace


def coin_flip_filter(data):
    coin_flips = np.random.randint(2, size=data.shape)
    bool_coin_flips = coin_flips.astype(np.bool)
    one_replace = np.where(bool_coin_flips, data, 1)
    return one_replace
