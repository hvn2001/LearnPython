import matplotlib.pyplot as plt

import pandas as pd


def read_dataframes():
    train_df = pd.read_csv('../weekly_sales.csv')
    features_df = pd.read_csv('../features.csv')
    stores_df = pd.read_csv('../stores.csv')
    return train_df, features_df, stores_df


train_df, features_df, stores_df = read_dataframes()
merged_features = features_df.merge(stores_df, on='Store')

features = ['Store', 'Date', 'IsHoliday']
final_dataset = train_df.merge(merged_features, on=features)
final_dataset = final_dataset.drop(columns=['Date'])
# ----------------------------------


plot_df = final_dataset[['Weekly_Sales', 'Type']]
plot_df = plot_df.groupby('Type').mean()
plot_df.plot.bar()
plt.title('Store Type vs. Weekly Sales')
plt.xlabel('Type')
plt.ylabel('Avg Weekly Sales (Dollars)')
plt.show()