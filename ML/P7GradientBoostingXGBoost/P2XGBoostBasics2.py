import numpy as np
import xgboost as xgb

print('------B. Using a Booster------')
# predefined evaluation data and labels
eval_data = np.array([
    [5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4,
     0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5],
    [4.9, 3., 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4,
     0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5],
    [4.7, 3.2, 1.3, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4,
     0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5],
    [4.6, 3.1, 1.5, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4,
     0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5],
])
eval_labels = np.array([0, 1, 0, 1])
print('Data shape: {}'.format(eval_data.shape))
print('Labels shape: {}'.format(eval_labels.shape))
deval = xgb.DMatrix(eval_data, label=eval_labels)

# Trained bst from previous code

dtrain = xgb.DMatrix(eval_data, label=eval_labels)
params = {
    'max_depth': 0,
    'objective': 'binary:logistic'
}
bst = xgb.train(params, dtrain)
print(bst.eval(deval))  # evaluation

# new_data contains 2 new data observations
new_data = np.array([
    [1.504e+01, 1.674e+01, 9.873e+01, 6.894e+02, 9.883e-02, 1.364e-01, 7.721e-02,
     6.142e-02, 1.668e-01, 6.869e-02, 3.720e-01, 8.423e-01, 2.304e+00, 3.484e+01,
     4.123e-03, 1.819e-02, 1.996e-02, 1.004e-02, 1.055e-02, 3.237e-03, 1.676e+01,
     2.043e+01, 1.097e+02, 8.569e+02, 1.135e-01, 2.176e-01, 1.856e-01, 1.018e-01,
     2.177e-01, 8.549e-02],
    [1.382e+01, 2.449e+01, 9.233e+01, 5.959e+02, 1.162e-01, 1.681e-01, 1.357e-01,
     6.759e-02, 2.275e-01, 7.237e-02, 4.751e-01, 1.528e+00, 2.974e+00, 3.905e+01,
     9.680e-03, 3.856e-02, 3.476e-02, 1.616e-02, 2.434e-02, 6.995e-03, 1.601e+01,
     3.294e+01, 1.060e+02, 7.880e+02, 1.794e-01, 3.966e-01, 3.381e-01, 1.521e-01,
     3.651e-01, 1.183e-01]
])
print('New shape: {}'.format(new_data.shape))
dpred = xgb.DMatrix(new_data)
# predictions represents probabilities
predictions = bst.predict(dpred)
print('{}\n'.format(predictions))
'''
Data shape: (119, 30)
Labels shape: (119,)
[0]	eval-error:0.226891
Data shape: [[1.504e+01 1.674e+01 9.873e+01 6.894e+02 9.883e-02 1.364e-01 7.721e-02
  6.142e-02 1.668e-01 6.869e-02 3.720e-01 8.423e-01 2.304e+00 3.484e+01
  4.123e-03 1.819e-02 1.996e-02 1.004e-02 1.055e-02 3.237e-03 1.676e+01
  2.043e+01 1.097e+02 8.569e+02 1.135e-01 2.176e-01 1.856e-01 1.018e-01
  2.177e-01 8.549e-02]
 [1.382e+01 2.449e+01 9.233e+01 5.959e+02 1.162e-01 1.681e-01 1.357e-01
  6.759e-02 2.275e-01 7.237e-02 4.751e-01 1.528e+00 2.974e+00 3.905e+01
  9.680e-03 3.856e-02 3.476e-02 1.616e-02 2.434e-02 6.995e-03 1.601e+01
  3.294e+01 1.060e+02 7.880e+02 1.794e-01 3.966e-01 3.381e-01 1.521e-01
  3.651e-01 1.183e-01]]
[0.6236573 0.6236573]
'''

print('------Ex: ------')
'''
dtrain = xgb.DMatrix(data, label=labels)  # Ex1
# Ex2
params = {
    'max_depth': 2,
    'objective': 'multi:softmax',
    'num_class': 3
}

bst = xgb.train(params, dtrain)  # Ex3
'''
