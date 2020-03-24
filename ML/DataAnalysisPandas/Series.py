import numpy as np
import pandas as pd

print('------A. 1-D data------')

series = pd.Series()
# Newline to separate series print statements
print('{}\n'.format(series))  # Series([], dtype: float64)

series = pd.Series(5)
print('{}\n'.format(series))
'''
0    5
dtype: int64
'''
series = pd.Series([1, 2, 3])
print('{}\n'.format(series))
'''
0    1
1    2
2    3
dtype: int64
'''

series = pd.Series([1, 2.2])  # upcasting
print('{}\n'.format(series))
'''
0    1.0
1    2.2
dtype: float64
'''

arr = np.array([1, 2])
series = pd.Series(arr, dtype=np.float32)
print('{}\n'.format(series))
'''
0    1.0
1    2.0
dtype: float32
'''

series = pd.Series([[1, 2], [3, 4]])
print('{}\n'.format(series))
'''
0    [1, 2]
1    [3, 4]
dtype: object
'''

print('------B. Index------')

series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print('{}\n'.format(series))
'''
a    1
b    2
c    3
dtype: int64
'''

series = pd.Series([1, 2, 3], index=['a', 8, 0.3])
print('{}\n'.format(series))
'''
a      1
8      2
0.3    3
dtype: int64
'''

print('------C. Dictionary input------')
series = pd.Series({'a': 1, 'b': 2, 'c': 3})
print('{}\n'.format(series))
'''
a    1
b    2
c    3
dtype: int64
'''

series = pd.Series({'b': 2, 'a': 1, 'c': 3})
print('{}\n'.format(series))
'''
a    1
b    2
c    3
dtype: int64
'''

print('------Ex: ------')
s1 = pd.Series([1, 3, 5.2])
s2 = s1 * [0.1, 0.2, 0.3]
s3 = pd.Series([1, 3, 8, np.nan], index=['a', 'b', 'c', 'd'])
s4 = pd.Series({'a': 0, 'b': 1, 'c': 2})
