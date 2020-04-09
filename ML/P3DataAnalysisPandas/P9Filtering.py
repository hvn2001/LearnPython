import pandas as pd
import numpy as np

print('------A. Filter conditions------')

df = pd.DataFrame({
    'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
    'yearID': [2016, 2016, 2016, 2016, 2017],
    'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
    'HR': [31, 39, 43, 38, 39]})

print('{}\n'.format(df))

cruzne02 = df['playerID'] == 'cruzne02'
print('{}\n'.format(cruzne02))

hr40 = df['HR'] > 40
print('{}\n'.format(hr40))

notbos = df['teamID'] != 'BOS'
print('{}\n'.format(notbos))

print('------B. Filters from functions------')
df = pd.DataFrame({
    'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
    'yearID': [2016, 2016, 2016, 2016, 2017],
    'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
    'HR': [31, 39, 43, 38, 39]})

print('{}\n'.format(df))

str_f1 = df['playerID'].str.startswith('c')
print('{}\n'.format(str_f1))

str_f2 = df['teamID'].str.endswith('S')
print('{}\n'.format(str_f2))

str_f3 = ~df['playerID'].str.contains('o')
print('{}\n'.format(str_f3))

print('------B. isin------')
df = pd.DataFrame({
    'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
    'yearID': [2016, 2016, 2016, 2016, 2017],
    'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
    'HR': [31, 39, 43, 38, 39]})

print('{}\n'.format(df))

isin_f1 = df['playerID'].isin(['cruzne02',
                               'ortizda01'])
print('{}\n'.format(isin_f1))

isin_f2 = df['yearID'].isin([2015, 2017])
print('{}\n'.format(isin_f2))

print('------B. use the isna and notna functions.------')
df = pd.DataFrame({
    'playerID': ['bettsmo01', 'canoro01', 'doejo01'],
    'yearID': [2016, 2016, 2017],
    'teamID': ['BOS', 'SEA', np.nan],
    'HR': [31, 39, 99]})

print('{}\n'.format(df))

isna = df['teamID'].isna()
print('{}\n'.format(isna))

notna = df['teamID'].notna()
print('{}\n'.format(notna))

print('------C. Feature filtering-------')
df = pd.DataFrame({
    'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'bettsmo01'],
    'yearID': [2016, 2016, 2016, 2016, 2015],
    'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'BOS'],
    'HR': [31, 39, 43, 38, 18]})

print('{}\n'.format(df))

hr40_df = df[df['HR'] > 40]
print('{}\n'.format(hr40_df))

not_hr30_df = df[~(df['HR'] > 30)]
print('{}\n'.format(not_hr30_df))

str_df = df[df['teamID'].str.startswith('B')]
print('{}\n'.format(str_df))

print('------Ex: -------')
# HVN defined
mlb_df = pd.DataFrame({
    'BA': [10, 15, 8],
    'H': [25, 27, 25],
    'AB': [16, 15, 10],

    '2B': [16, 15, 10],
    '3B': [16, 15, 10],
    'HR': [16, 15, 10],
    'playerID': ['bettsmo01', 'canoro01', 'cruzne02']
})

top_hitters = mlb_df[mlb_df['BA'] > .300]

exclude_a = mlb_df[~mlb_df['playerID'].str.startswith('a')]

two_ids = ['bondsba01', 'troutmi01']
two_players = mlb_df[mlb_df['playerID'].isin(two_ids)]
