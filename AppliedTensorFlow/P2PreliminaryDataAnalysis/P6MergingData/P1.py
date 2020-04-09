import pandas as pd


def read_dataframes():
    train_df = pd.read_csv('../weekly_sales.csv')
    features_df = pd.read_csv('../features.csv')
    stores_df = pd.read_csv('../stores.csv')
    return train_df, features_df, stores_df


train_df, features_df, stores_df = read_dataframes()
merged_features = features_df.merge(stores_df, on='Store')
# ---------


train_df = pd.read_csv('weekly_sales.csv')
print(train_df.columns.tolist())

# Merged and imputed stores + features
print(merged_features.columns.tolist())
