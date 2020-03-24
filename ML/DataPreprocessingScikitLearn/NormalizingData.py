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
'''
array([[4, 1, 2, 2],
       [3, 4, 0, 0],
       [7, 5, 9, 2]])

array([[0.8       , 0.2       , 0.4       , 0.4       ],
       [0.6       , 0.8       , 0.        , 0.        ],
       [0.55513611, 0.39652579, 0.71374643, 0.15861032]])
'''
print('------Ex: ------')


def normalize_data(data):
    normalizer = Normalizer()
    norm_data = normalizer.fit_transform(data)
    return norm_data
