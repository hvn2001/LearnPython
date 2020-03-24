import pandas as pd
import numpy as np

print('------A. Sorting by feature------')
df = pd.DataFrame({
    'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
    'yearID': [2016, 2016, 2016, 2016, 2017],
    'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
    'HR': [31, 39, 43, 38, 39]})
print('{}\n'.format(df))

sort1 = df.sort_values('yearID')
print('{}\n'.format(sort1))

sort2 = df.sort_values('playerID', ascending=False)
print('{}\n'.format(sort2))

print('------A. sort with a list of column labels------')
print('{}\n'.format(df))

sort1 = df.sort_values(['yearID', 'playerID'])
print('{}\n'.format(sort1))

sort2 = df.sort_values(['yearID', 'HR'],
                       ascending=[True, False])
print('{}\n'.format(sort2))

print('------Ex: -------')
yearly_stats_df = pd.DataFrame({
    'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
    'yearID': [2016, 2016, 2016, 2016, 2017],
    'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
    'HR': [31, 39, 43, 38, 39],
    'SO': [31, 39, 43, 38, 39]})
by_year = yearly_stats_df.sort_values('yearID')

best_hr = yearly_stats_df.sort_values('HR', ascending=False)

best_hr_so = yearly_stats_df.sort_values(['HR', 'SO'],
                                         ascending=[False, True])
