import pandas as pd

print('------A. Direct indexing------')

df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]}, index=['r1', 'r2'])
col1 = df['c1']
print('{}\n'.format(col1))
'''
r1    1
r2    2
Name: c1, dtype: int64
'''

col1_df = df[['c1']]
print('{}\n'.format(col1_df))
'''
    c1
r1   1
r2   2
'''

col23 = df[['c2', 'c3']]
print('{}\n'.format(col23))
'''
    c2  c3
r1   3   5
r2   4   6
'''

print('------A. directly index into a DataFrame''s rows------')

df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])

print('{}\n'.format(df))
'''
    c1  c2  c3
r1   1   4   7
r2   2   5   8
r3   3   6   9
'''

first_two_rows = df[0:2]
print('{}\n'.format(first_two_rows))
'''
    c1  c2  c3
r1   1   4   7
r2   2   5   8
'''

last_two_rows = df['r2':'r3']
print('{}\n'.format(last_two_rows))
'''
    c1  c2  c3
r2   2   5   8
r3   3   6   9
'''

# Results in KeyError
# df['r1']

print('------B. Other indexing------')
df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])

print('{}\n'.format(df))
'''
    c1  c2  c3
r1   1   4   7
r2   2   5   8
r3   3   6   9
'''

print('{}\n'.format(df.iloc[1]))
'''
c1    2
c2    5
c3    8
Name: r2, dtype: int64
'''

print('{}\n'.format(df.iloc[[0, 2]]))
'''
    c1  c2  c3
r1   1   4   7
r3   3   6   9
'''

bool_list = [False, True, True]
print('{}\n'.format(df.iloc[bool_list]))
'''
    c1  c2  c3
r2   2   5   8
r3   3   6   9
'''

print('------B.  usages of loc------')

df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])

print('{}\n'.format(df))
'''
    c1  c2  c3
r1   1   4   7
r2   2   5   8
r3   3   6   9
'''

print('{}\n'.format(df.loc['r2']))
'''
c1    2
c2    5
c3    8
Name: r2, dtype: int64
'''

bool_list = [False, True, True]
print('{}\n'.format(df.loc[bool_list]))
'''
    c1  c2  c3
r2   2   5   8
r3   3   6   9
'''

single_val = df.loc['r1', 'c2']
print('Single val: {}\n'.format(single_val))  # Single val: 4

print('{}\n'.format(df.loc[['r1', 'r3'], 'c2']))
'''
r1    4
r3    6
Name: c2, dtype: int64
'''

df.loc[['r1', 'r3'], 'c2'] = 0
print('{}\n'.format(df))
'''
    c1  c2  c3
r1   1   0   7
r2   2   5   8
r3   3   0   9
'''

print('------Ex: ------')
col_1 = df['c1']
row_12 = df[0:2]

row_13 = df.iloc[[0, 2]]
# df.loc[['r3', 'r4'], 'c2'] = 12
