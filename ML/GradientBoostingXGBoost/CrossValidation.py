import numpy as np
import xgboost as xgb

print('------A. Choosing parameters------')

# predefined data and labels
data = np.array([
    [5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4,
     0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5],
    [4.9, 3., 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4,
     0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5],
    [4.7, 3.2, 1.3, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4,
     0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5],
    [4.6, 3.1, 1.5, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4,
     0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5],
])
labels = np.array([0, 1, 0, 1])
dtrain = xgb.DMatrix(data, label=labels)
params = {
    'max_depth': 2,
    'lambda': 1.5,
    'objective': 'binary:logistic'
}
cv_results = xgb.cv(params, dtrain)
print('CV Results:\n{}'.format(cv_results))

print('------A. num_boost_round------')
# predefined data and labels
dtrain = xgb.DMatrix(data, label=labels)
params = {
    'max_depth': 2,
    'lambda': 1.5,
    'objective': 'binary:logistic'
}
cv_results = xgb.cv(params, dtrain, num_boost_round=5)
print('CV Results:\n{}'.format(cv_results))
