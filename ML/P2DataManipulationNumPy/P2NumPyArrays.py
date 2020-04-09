import numpy as np

print('----A. Arrays----')
arr = np.array([[0, 1, 2], [3, 4, 5]],
               dtype=np.float32)
print(repr(arr))

arr = np.array([0, 0.1, 2])  # np.array upcasting.
print(repr(arr))

print('----B. Copying: b.copy()----')
a = np.array([0, 1])
b = np.array([9, 8])
c = a
print('Array a: {}'.format(repr(a)))
c[0] = 5
print('Array a: {}'.format(repr(a)))

d = b.copy()
d[0] = 6
print('Array b: {}'.format(repr(b)))

print('----C. Casting: arr.astype(np.)----')
arr = np.array([0, 1, 2])
print(arr.dtype)
arr = arr.astype(np.float32)
print(arr.dtype)

print('----D. NaN----')
arr = np.array([np.nan, 1, 2])
print(repr(arr))

arr = np.array([np.nan, 'abc'])
print(repr(arr))

# Will result in a ValueError
# np.array([np.nan, 1, 2], dtype=np.int32)

print('----E. Infinity: np.inf----')
print(np.inf > 1000000)

arr = np.array([np.inf, 5])
print(repr(arr))

arr = np.array([-np.inf, 1])
print(repr(arr))

# Will result in an OverflowError
# np.array([np.inf, 3], dtype=np.int32)

print('----Exe----')
arr = np.array([np.nan, 2, 3, 4, 5])
arr2 = arr.copy()
arr2[0] = 10
float_arr = np.array([1, 5.4, 3])
float_arr2 = arr2.astype(np.float32)

matrix = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
# matrix = matrix.astype(np.float32)
print(repr(matrix))
