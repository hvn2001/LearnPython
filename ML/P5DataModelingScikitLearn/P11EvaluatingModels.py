from sklearn import tree
import pandas as pd
import numpy as np

print('------A. Making predictions------')

train_data = pd.DataFrame([[2100, 800],
                           [2500, 850],
                           [1800, 760],
                           [2000, 800],
                           [2300, 810]],
                          )

train_labels = pd.DataFrame([10.99, 12.5, 9.99, 10.99, 11.99])
test_data = np.array([[2000, 820],
                      [2200, 830]])

reg = tree.DecisionTreeRegressor()
# predefined train and test sets
reg.fit(train_data, train_labels)
predictions = reg.predict(test_data)

print('------B. Evaluation metrics------')

test_labels = pd.DataFrame([2000, 820])
reg = tree.DecisionTreeRegressor()
# predefined train and test sets
reg.fit(train_data, train_labels)
predictions = reg.predict(test_data)

from sklearn import metrics

r2 = metrics.r2_score(test_labels, predictions)
print('R2: {}\n'.format(r2))
mse = metrics.mean_squared_error(
    test_labels, predictions)
print('MSE: {}\n'.format(mse))
mae = metrics.mean_absolute_error(
    test_labels, predictions)
print('MAE: {}\n'.format(mae))
'''
R2: 0.624959156484117

MSE: 26.484251968503937

MAE: 3.119685039370079
'''

print('------B. evaluates a classification model''s predictions based on the testing labels------')
train_data = pd.DataFrame([[2100, 800],
                           [2500, 850],
                           [1800, 760],
                           [2000, 800],
                           [2300, 810]],
                          )

train_labels = pd.DataFrame([800, 2500, 760, 2000, 2300])
test_labels = pd.DataFrame([[2000, 820, 820]])
test_data = np.array([[2000, 820],
                      [2200, 830]])

print('{}\n'.format(train_data))
print('{}\n'.format(train_labels))
print('{}\n'.format(test_labels))

clf = tree.DecisionTreeClassifier()
# predefined train and test sets
clf.fit(train_data, train_labels)
predictions = clf.predict(test_data)

from sklearn import metrics

acc = metrics.accuracy_score(test_labels,
                             predictions)  # ValueError: Found input variables with inconsistent numbers of samples: [1, 2]
print('Accuracy: {}\n'.format(acc))
