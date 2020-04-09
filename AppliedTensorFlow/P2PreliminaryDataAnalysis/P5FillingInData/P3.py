import numpy as np  # NumPy library

import pandas as pd


def read_dataframes():
    train_df = pd.read_csv('../weekly_sales.csv')
    features_df = pd.read_csv('../features.csv')
    stores_df = pd.read_csv('../stores.csv')
    return train_df, features_df, stores_df


train_df, features_df, stores_df = read_dataframes()
merged_features = features_df.merge(stores_df, on='Store')
na_values = pd.isna(merged_features)  # Boolean DataFrame
na_features = na_values.any()  # Boolean Series

na_cpi_int = na_values['CPI'].astype(int)
na_indexes_cpi = na_cpi_int.to_numpy().nonzero()[0]
na_une_int = na_values['Unemployment'].astype(int)
na_indexes_une = na_une_int.to_numpy().nonzero()[0]

na_indexes = na_indexes_cpi

# 


print(na_indexes[0])  # first missing value row index
print()

first_missing_row = merged_features.iloc[169]
print(first_missing_row[['Date', 'CPI', 'Unemployment']])
print()

final_val_row = merged_features.iloc[168]
print(final_val_row[['Date', 'CPI', 'Unemployment']])
print()

cpi_final_val = merged_features.at[168, 'CPI']
une_final_val = merged_features.at[168, 'Unemployment']
merged_features.at[169, 'CPI'] = cpi_final_val
merged_features.at[169, 'Unemployment'] = une_final_val

new_row = merged_features.iloc[169]
print(new_row[['Date', 'CPI', 'Unemployment']])
print()
