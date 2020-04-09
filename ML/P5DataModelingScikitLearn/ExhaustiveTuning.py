import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn import linear_model

print('------A. Grid-search cross-validation------')
# From TrainingTesting
data = np.array([
    [10.2, 0.5],
    [8.7, 0.9],
    [9.3, 0.8],
    [10.1, 0.4],
    [9.5, 0.77],
    [9.1, 0.68],
    [7.7, 0.9],
    [8.3, 0.8]])
labels = np.array(
    [1.4, 1.2, 1.6, 1.5, 1.6, 1.3, 1.1, 1.2])
from sklearn.model_selection import train_test_split

split_dataset = train_test_split(data, labels)
train_data = split_dataset[0]
train_labels = split_dataset[2]

print('{}\n'.format(train_data))
print('{}\n'.format(train_labels))

reg = linear_model.BayesianRidge()
params = {
    'alpha_1': [0.1, 0.2, 0.3],
    'alpha_2': [0.1, 0.2, 0.3]
}
reg_cv = GridSearchCV(reg, params, cv=5, iid=False)
# predefined train and test sets
reg_cv.fit(train_data, train_labels)  # UndefinedMetricWarning: R^2 score is not well-defined with less than two samples
# FutureWarning: The parameter 'iid' is deprecated in 0.22 and will be removed in 0.24.
print(reg_cv.best_params_)
