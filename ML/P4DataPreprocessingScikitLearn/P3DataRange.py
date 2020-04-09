import pandas as pd

print('------B. Range compression in scikit-learn------')

data = pd.DataFrame({'HR': [1.2, -0.3, 6.5, 2.2],
                     'HR2': [3.2, -1.2, 10.1, -8.4],
                     'HR4': [100, 100, 100, 200]})
print('{}\n'.format(repr(data)))

from sklearn.preprocessing import MinMaxScaler

default_scaler = MinMaxScaler()  # the default range is [0,1]
transformed = default_scaler.fit_transform(data)
print('{}\n'.format(repr(transformed)))

custom_scaler = MinMaxScaler(feature_range=(-2, 3))
transformed = custom_scaler.fit_transform(data)
print('{}\n'.format(repr(transformed)))

print('------B.run the fit and transform functions separately and compare them with the fit_transform function------')
new_data = pd.DataFrame({'HR': [1.2, 5.3, -3.3],
                         'HR2': [-0.5, 2.3, 4.1],
                         'HR4': [100, 100, 200]})
print('{}\n'.format(repr(new_data)))

from sklearn.preprocessing import MinMaxScaler

default_scaler = MinMaxScaler()  # the default range is [0,1]
transformed = default_scaler.fit_transform(new_data)
print('{}\n'.format(repr(transformed)))

default_scaler = MinMaxScaler()  # new instance
default_scaler.fit(data)  # different data value fit
transformed = default_scaler.transform(new_data)
print('{}\n'.format(repr(transformed)))

print('------Ex: ------')


def ranged_data(data, value_range):
    min_max_scaler = MinMaxScaler(feature_range=value_range)
    scaled_data = min_max_scaler.fit_transform(data)
    return scaled_data
