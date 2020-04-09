import pandas as pd

print('------A. Machine learning------')
print('------B. Indicator features------')

df = pd.DataFrame({'teamID_BOS': [1, 2, 3, 3], 'teamID_PIT': [4, 5, 6, 6],
                   'lgID_AL': [7, 8, 9, 9], 'lgID_NL': [10, 11, 12, 14]},
                  index=['r1', 'r2', 'r3', 'r4'])
print('{}\n'.format(df))

indicator_df = pd.DataFrame({
    'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
    'HR': [80, 39, 43, 38, 60],
    'SO': [31, 39, 43, 38, 39],
    'RBI': [80, 100, 12, 16, 18]})
print('{}\n'.format(indicator_df))

print('------C. Converting to indicators------')
print('{}\n'.format(df))

converted = pd.get_dummies(df)
print('{}\n'.format(converted.columns))

print('{}\n'.format(converted[['teamID_BOS',
                               'teamID_PIT']]))
print('{}\n'.format(converted[['lgID_AL',
                               'lgID_NL']]))

print('------D. Converting to NumPy------')
print('{}\n'.format(df))

n_matrix = df.values
print(repr(n_matrix))

print('------Ex: ------')
df = pd.DataFrame({'name': ['Mo', 'Susu', 'Ro', 'HVN'],
                   'pos': ['VN', 'HCM', 'VN', 'HCM'],
                   'yearID': [2000, 2004, 2016, 2016]})
df = df[df['yearID'] >= 2000]  # Ex1

df = df.dropna()  # Ex2

df = pd.get_dummies(df)  # Ex3
matrix = df.values
