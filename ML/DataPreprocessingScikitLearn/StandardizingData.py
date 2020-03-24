import pandas as pd

print('------B. NumPy and scikit-learn------')
pizza_data = pd.DataFrame({'HR': [2100, 2500, 1800, 2000, 2300],
                           'HR2': [10, 11, 10, 12, 11],
                           'HR3': [800, 850, 760, 800, 810],
                           'HR4': [100, 100, 100, 100, 200]})
# Newline to separate print statements
print('{}\n'.format(repr(pizza_data)))

from sklearn.preprocessing import scale

# Standardizing each column of pizza_data
col_standardized = scale(pizza_data)
print('{}\n'.format(repr(col_standardized)))

# Column means (rounded to nearest thousandth)
col_means = col_standardized.mean(axis=0).round(decimals=3)
print('{}\n'.format(repr(col_means)))

# Column standard deviations
col_stds = col_standardized.std(axis=0)
print('{}\n'.format(repr(col_stds)))

print('------Ex: ------')


def standardize_data(data):
    scaled_data = scale(data)
    return scaled_data
