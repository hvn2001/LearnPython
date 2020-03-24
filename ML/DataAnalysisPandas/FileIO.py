import pandas as pd

print('------A. Reading data------')

# data.csv contains baseball data
df = pd.read_csv('data.csv')
print('{}\n'.format(df))
'''
   HR       name pos
0  17  joe smith  2B
1  28  alan west   C
2  19   john doe   P
'''

df = pd.read_csv('data.csv', index_col=0)
print('{}\n'.format(df))
'''
         name pos
HR               
17  joe smith  2B
28  alan west   C
19   john doe   P
'''

df = pd.read_csv('data.csv', index_col=1)
print('{}\n'.format(df))
'''
           HR pos
name             
joe smith  17  2B
alan west  28   C
john doe   19   P
'''

print('-------A. Reading Excel pd.read_excel------')
# data.csv contains baseball data
df = pd.read_excel('data.xlsx')
print('{}\n'.format(df))
'''
   HR       name pos
0   1   jack lee  SS
1  52     mo sam  1B
2  37  lex jones  RF
'''

print('Sheet 1 (0-indexed) DataFrame:')
df = pd.read_excel('data.xlsx', sheet_name=1)
print('{}\n'.format(df))
'''
   HR        name pos
0  32    abe hass  LF
1  17    jim buck   C
2  58  aaron dean  LF
'''

print('MIL DataFrame:')
df = pd.read_excel('data.xlsx', sheet_name='MIL')
print('{}\n'.format(df))
'''
   HR         name pos
0  15      jj west  LF
1  44  will thomas  CF
2  12   alex stein  3B
'''

# Sheets 0 and 1
df_dict = pd.read_excel('data.xlsx', sheet_name=[0, 1])
print('{}\n'.format(df_dict[1]))
'''
   HR        name pos
0  32    abe hass  LF
1  17    jim buck   C
2  58  aaron dean  LF
'''

# All Sheets
df_dict = pd.read_excel('data.xlsx', sheet_name=None)
print(df_dict.keys())
'''
odict_keys(['NYY', 'BOS', 'MIL'])
'''

print('-------A. Reading JSON : orient=''index''------')
# data is the JSON data (as a Python dict)
# print('{}\n'.format(data))

df1 = pd.read_json('data.json')
print('{}\n'.format(df1))
'''
    jack doe tom june
HR         4       31
pos       1B        P
'''

df2 = pd.read_json('data.json', orient='index')
print('{}\n'.format(df2))
'''
          HR pos
jack doe   4  1B
tom june  31   P
'''
mlb_df = pd.read_csv('data.csv')
print('------B. Writing to files------')
print('------CSV------')
# Predefined mlb_df
print('{}\n'.format(mlb_df))
'''
   HR       name pos
0  17  joe smith  2B
1  28  alan west   C
2  19   john doe   P
'''

# Index is kept when writing
mlb_df.to_csv('data_out.csv')
df = pd.read_csv('data_out.csv')
print('{}\n'.format(df))
'''
   Unnamed: 0  HR       name pos
0           0  17  joe smith  2B
1           1  28  alan west   C
2           2  19   john doe   P
'''

# Index is not kept when writing
mlb_df.to_csv('data_out.csv', index=False)
df = pd.read_csv('data_out.csv')
print('{}\n'.format(df))
'''
   HR       name pos
0  17  joe smith  2B
1  28  alan west   C
2  19   john doe   P
'''

print('------Excel------')
mlb_df1 = pd.read_excel('data.xlsx')
mlb_df2 = pd.read_excel('data.xlsx', sheet_name=1)
print('{}\n'.format(mlb_df1))
print('{}\n'.format(mlb_df2))

with pd.ExcelWriter('data_out.xlsx') as writer:
    mlb_df1.to_excel(writer, index=False, sheet_name='NYY1')
    mlb_df2.to_excel(writer, index=False, sheet_name='BOS1')

df_dict = pd.read_excel('data_out.xlsx', sheet_name=None)
print(df_dict.keys())
print('{}\n'.format(df_dict['BOS1']))

print('------JSON------')
df = pd.read_json('data.json')
print('{}\n'.format(df))

df.to_json('data_out.json')
df2 = pd.read_json('data_out.json')
print('{}\n'.format(df2))

df.to_json('data_out2.json', orient='index')  # write to file
df2 = pd.read_json('data_out2.json')
print('{}\n'.format(df2))
df2 = pd.read_json('data_out.json', orient='index')
print('{}\n'.format(df2))