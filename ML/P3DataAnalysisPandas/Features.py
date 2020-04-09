import pandas as pd

print('------A. Quantitative vs. categorical------')

print('------B. Quantitative features------')

df = pd.DataFrame({
    'T1': [10, 15, 8],
    'T2': [25, 27, 25],
    'T3': [16, 15, 10]})

print('{}\n'.format(df))

print('{}\n'.format(df.sum()))

print('{}\n'.format(df.sum(axis=1)))

print('{}\n'.format(df.mean()))

print('{}\n'.format(df.mean(axis=1)))

print('------C. Weighted features------')
df = pd.DataFrame({
    'T1': [0.1, 150.],
    'T2': [0.25, 240.],
    'T3': [0.16, 100.]})

print('{}\n'.format(df))

print('{}\n'.format(df.multiply(2)))

df_ms = df.multiply([1000, 1], axis=0)
print('{}\n'.format(df_ms))

df_w = df_ms.multiply([1, 0.5, 1])
print('{}\n'.format(df_w))
print('{}\n'.format(df_w.sum(axis=1)))

print('------Ex: ------')
# HVN defined
mlb_df = pd.DataFrame({
    'BA1': [10, 15, 8],
    'H': [25, 27, 25],
    'AB': [16, 15, 10],

    '2B': [16, 15, 10],
    '3B': [16, 15, 10],
    'HR': [16, 15, 10]
})


def col_list_sum(df, col_list, weights=None):
    col_df = df[col_list]
    if weights is not None:
        col_df = col_df.multiply(weights)
    return col_df.sum(axis=1)


mlb_df['BA'] = mlb_df['H'] / mlb_df['AB']

other_hits = col_list_sum(mlb_df, ['2B', '3B', 'HR'])
mlb_df['1B'] = mlb_df['H'] - other_hits

weighted_hits = col_list_sum(mlb_df, ['1B', '2B', '3B', 'HR'],
                             weights=[1, 2, 3, 4])

mlb_df['SLG'] = weighted_hits / mlb_df['AB']
