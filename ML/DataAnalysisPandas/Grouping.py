import pandas as pd
import numpy as np

print('------A. Grouping by column------')
'''
df = pd.DataFrame({'name': ['Mo', 'Susu', 'Ro', 'HVN'],
                   'pos': ['VN', 'HCM', 'VN', 'HCM'],
                   'yearID': [2000, 2004, 2016, 2016]})
'''
df = pd.DataFrame({'A': [11, 12, 13, 14, 15],
                   'B': [np.nan, 2, 3, 4, 5],
                   'yearID': [1, 2016, 1, 1, 2016]}, columns=['A', 'B', 'yearID'])
print('{}\n'.format(df))

groups = df.groupby('yearID')
for name, group in groups:
    print('Year: {}'.format(name))
    print('{}\n'.format(group))

print('get_group: \n{}\n'.format(groups.get_group(2016)))
print('sum: \n{}\n'.format(groups.sum()))
print('mean: \n{}\n'.format(groups.mean()))

print('------A. use the filter------')
no2015 = groups.filter(lambda x: x.name > 2015)
print(no2015)

print('------B. Multiple columns------')
player_df = pd.DataFrame({'teamID': ['REAL', 'REAL', 'REAL', 'REAL', 'REAL'],
                          'B': [np.nan, 2, 3, 4, 5],
                          'yearID': [1, 2016, 1, 1, 2016]}, columns=['teamID', 'B', 'yearID'])
groups = player_df.groupby(['yearID', 'teamID'])

for name, group in groups:
    print('Year, Team: {}'.format(name))
    print('{}\n'.format(group))

print('->Sum: \n{}\n'.format(groups.sum()))

print('------Ex: ------')
year_group = df.groupby('yearID')
year_stats = year_group.sum()
hr_2017 = year_stats.loc[2017, 'HR']
year_team_group = df.groupby(['yearID', 'teamID'])
year_team_stats = year_team_group.sum()
