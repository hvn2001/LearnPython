import pandas as pd

print('------B. Scored cross-validation------')
data = pd.DataFrame([[2100, 800],
                     [2500, 850],
                     [1800, 760],
                     [2000, 800],
                     [2300, 810]],
                    )
# labels = pd.DataFrame([10, 12, 9, 10, 11]).values.ravel()  # HVN ? 2 x '10' -> ValueError: n_splits=3 cannot be greater than the number of members in each class.
labels = pd.DataFrame([10, 12, 9, 10, 10]).values.ravel()

from sklearn import linear_model
from sklearn.model_selection import cross_val_score

clf = linear_model.LogisticRegression()
# Predefined data and labels
cv_score = cross_val_score(clf, data, labels, cv=3)  # k = 3

print('{}\n'.format(repr(cv_score)))

'''array([0.93684211, 0.96842105, 0.94179894])'''

print('------B. K-Fold CV with 4 folds------')

from sklearn import linear_model
from sklearn.model_selection import cross_val_score

reg = linear_model.LinearRegression()
# Predefined data and labels
cv_score = cross_val_score(reg, data, labels, cv=4)  # k = 4  #  UndefinedMetricWarning: R^2 score is not well-defined with less than two samples.

print('{}\n'.format(repr(cv_score)))

'''array([0.37548118, 0.49022643, 0.52061242, 0.54864085])'''
