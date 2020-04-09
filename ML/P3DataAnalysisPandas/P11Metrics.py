import pandas as pd
import numpy as np

print('------A. Numeric metrics------')
df = pd.DataFrame({
    'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
    'yearID': [2016, 2016, 2016, 2016, 2017],
    'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
    'HR': [31, 39, 43, 38, 39],
    'SO': [31, 39, 43, 38, 39],
    'RBI': [80, 100, 12, 16, 18]})
print('{}\n'.format(df))

metrics1 = df.describe()
print('{}\n'.format(metrics1))

hr_rbi = df[['HR', 'RBI']]
metrics2 = hr_rbi.describe()
print('{}\n'.format(metrics2))

print('------A. percentiles  keyword------')
metrics1 = hr_rbi.describe(percentiles=[.5])
print('{}\n'.format(metrics1))

metrics2 = hr_rbi.describe(percentiles=[.1])
print('{}\n'.format(metrics2))

metrics3 = hr_rbi.describe(percentiles=[.2, .8])
print('{}\n'.format(metrics3))

print('------B. Categorical features------')
p_ids = df['playerID']
print('{}\n'.format(p_ids.value_counts()))

print('{}\n'.format(p_ids.value_counts(normalize=True)))

print('{}\n'.format(p_ids.value_counts(ascending=True)))

print('------B. use the unique function------')
unique_players = df['playerID'].unique()
print('{}\n'.format(repr(unique_players)))

unique_teams = df['teamID'].unique()
print('{}\n'.format(repr(unique_teams)))

print('------B. can use yearID as a categorical feature with each unique year as a separate category------')
y_ids = df['yearID']
print('{}\n'.format(y_ids))

print('{}\n'.format(repr(y_ids.unique())))
print('{}\n'.format(y_ids.value_counts()))

print('------Ex: -------')
player_df = pd.DataFrame({
    'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
    'yearID': [2016, 2016, 2016, 2016, 2017],
    'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
    'HR': [31, 39, 43, 38, 39],
    'SO': [31, 39, 43, 38, 39],
    'RBI': [80, 100, 12, 16, 18]})
print('------Ex1: -------')
summary_all = player_df.describe()

print('------Ex2: -------')
hr_df = player_df['HR']
summary_hr = hr_df.describe()
low_high_10 = hr_df.describe(percentiles=[.1, .9])

print('------Ex3: -------')
hr_counts = hr_df.value_counts()
