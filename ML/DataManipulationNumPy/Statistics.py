import numpy as np

print('----A. Analysis----')

arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])
print(arr.min())
print(arr.max())

print(repr(arr.min(axis=0)))  # array([ -3,  -2, -60])
print(repr(arr.max(axis=-1)))  # array([72,  3,  4])

print('----B. Statistical metrics----')

arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])
print(np.mean(arr))
print(np.var(arr))
print(np.median(arr))
print(repr(np.median(arr, axis=-1)))

print('----Ex: ----')


def get_min_max(data):
    overall_min = data.min()
    overall_max = data.max()
    return overall_min, overall_max


def col_min(data):
    min0 = data.min(axis=0)
    return min0


def basic_stats(data):
    mean = np.mean(data)
    median = np.median(data)
    var = np.var(data)
    return mean, median, var
