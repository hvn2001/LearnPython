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

# --------------

markdowns = [
    'MarkDown1',
    'MarkDown2',
    'MarkDown3',
    'MarkDown4',
    'MarkDown5'
]
merged_features = merged_features.drop(columns=markdowns)
print(merged_features.columns.tolist())
