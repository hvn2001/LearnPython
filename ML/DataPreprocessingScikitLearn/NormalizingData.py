import pandas as pd

print('------A. Data outliers------')
data = pd.DataFrame({'HR': [4, 3, 7],
                     'HR2': [1, 4, 5],
                     'HR4': [2, 0, 9],
                     'HR5': [2, 0, 2]})
print('{}\n'.format(repr(data)))

from sklearn.preprocessing import Normalizer

normalizer = Normalizer()
transformed = normalizer.fit_transform(data)
print('{}\n'.format(repr(transformed)))

print('------Ex: ------')


def normalize_data(data):
    normalizer = Normalizer()
    norm_data = normalizer.fit_transform(data)
    return norm_data
