import pandas as pd

print('------A. Data outliers------')
print('------B. Robust scaling with scikit-learn------')
data = pd.DataFrame({'HR': [1.2, 2.1, -1.9, -2.5, 0.8, 6.3, -1.5, 1.4, 1.8],
                     'HR2': [2.3, 4.2, 3.1, 2.5, 3., 2.1, 2.7, 2.9, 3.2]})
print('{}\n'.format(repr(data)))

from sklearn.preprocessing import RobustScaler

robust_scaler = RobustScaler()
transformed = robust_scaler.fit_transform(data)
print('{}\n'.format(repr(transformed)))

print('------Ex: ------')


def robust_scaling(data):
    robust_scaler = RobustScaler()
    scaled_data = robust_scaler.fit_transform(data)
    return scaled_data
