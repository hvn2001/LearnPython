import pandas as pd

print('------A. 2-D data------')
df = pd.DataFrame()
# Newline added to separate DataFrames
print('{}\n'.format(df))
'''
Empty DataFrame
Columns: []
Index: []
'''

df = pd.DataFrame([5, 6])
print('{}\n'.format(df))
'''
   0
0  5
1  6
'''

df = pd.DataFrame([[5, 6], [50, 60]])
print('{}\n'.format(df))
'''
    0   1
1  50  60
1  50  60
'''

df = pd.DataFrame([[5, 6], [1, 3]],
                  index=['r1', 'r2'],
                  columns=['c1', 'c2'])
print('{}\n'.format(df))
'''
    c1  c2
r1   5   6
r2   1   3
'''

df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4]},
                  index=['r1', 'r2'])
print('{}\n'.format(df))
'''
    c1  c2
r1   1   3
r2   2   4
'''

print('------B. Upcasting------')
upcast = pd.DataFrame([[5, 6], [1.2, 3]])
print('{}\n'.format(upcast))
'''
     0  1
0  5.0  6
1  1.2  3
'''

# Datatypes of each column
print(upcast.dtypes)
'''
0    float64
1      int64
dtype: object
'''

print('------C. Appending rows------')
df = pd.DataFrame([[5, 6], [1.2, 3]])
ser = pd.Series([0, 0], name='r3')

df_app = df.append(ser)
print('{}\n'.format(df_app))
'''
      0  1
0   5.0  6
1   1.2  3
r3  0.0  0
'''

df_app = df.append(ser, ignore_index=True)
print('{}\n'.format(df_app))
'''
     0  1
0  5.0  6
1  1.2  3
2  0.0  0
'''

df2 = pd.DataFrame([[0, 0], [9, 9]])
df_app = df.append(df2)
print('{}\n'.format(df_app))
'''
     0  1
0  5.0  6
1  1.2  3
0  0.0  0
1  9.0  9
'''

print('------D. Dropping data------')
df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]},
                  index=['r1', 'r2'])
'''
    c1  c2  c3
r1   1   3   5    
r2   2   4   6
'''

# Drop row r1
df_drop = df.drop(labels='r1')
print('{}\n'.format(df_drop))
'''
    c1  c2  c3
r2   2   4   6
'''

# Drop columns c1, c3
df_drop = df.drop(labels=['c1', 'c3'], axis=1)  # axis is mandatory because use labels=['c1',..]
print('{}\n'.format(df_drop))
'''
    c2
r1   3
r2   4
'''

df_drop = df.drop(index='r2')
print('{}\n'.format(df_drop))
'''
    c1  c2  c3
r1   1   3   5
'''

df_drop = df.drop(columns='c2')
print('{}\n'.format(df_drop))
'''
    c1  c3
r1   1   5
r2   2   6
'''

df_drop = df.drop(index='r2', columns='c2')
print('{}\n'.format(df_drop))
'''
    c1  c3
r1   1   5
'''

print('------Ex: ------')
df = pd.DataFrame({'c1': [0, 1, 2, 3], 'c2': [5, 6, 7, 8]}, index=['r1', 'r2', 'r3', 'r4'])
row_df = pd.DataFrame([[9, 9]], columns=['c1', 'c2'], index=['r5'])
df_app = df.append(row_df)
df_drop = df_app.drop(labels='r2')
