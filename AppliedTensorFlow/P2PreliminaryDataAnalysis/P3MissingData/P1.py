import pandas as pd


def read_dataframes():
    train_df = pd.read_csv('../weekly_sales.csv')
    features_df = pd.read_csv('../features.csv')
    stores_df = pd.read_csv('../stores.csv')
    return train_df, features_df, stores_df


train_df, features_df, stores_df = read_dataframes()

general_features = features_df.columns

print(general_features)
print('General Features: {}\n'.format(general_features.tolist()))

store_features = stores_df.columns
print('Store Features: {}'.format(store_features.tolist()))
