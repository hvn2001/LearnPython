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
# ------------------------

plot_df = final_dataset[['Weekly_Sales', 'Temperature']]
rounded_temp = plot_df['Temperature'].round(0)  # nearest integer
plot_df = plot_df.groupby(rounded_temp).mean()
plot_df.plot.scatter(x='Temperature', y='Weekly_Sales')
plt.show()
