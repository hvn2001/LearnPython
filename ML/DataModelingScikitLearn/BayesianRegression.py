import pandas as pd

print('------C. Tuning the model------')
data = pd.DataFrame([[2100, 800],
                     [2500, 850],
                     [1800, 760],
                     [2000, 800],
                     [2300, 810]],
                    )
labels = pd.DataFrame([10.99, 12.5, 9.99, 10.99, 11.99]).values.ravel()  # HVN ?

print('Data shape: {}\n'.format(data.shape))
print('Labels shape: {}\n'.format(labels.shape))

from sklearn import linear_model

reg = linear_model.BayesianRidge()
reg.fit(data, labels)
print('Coefficients: {}\n'.format(repr(reg.coef_)))
print('Intercept: {}\n'.format(reg.intercept_))
print('R2: {}\n'.format(reg.score(data, labels)))
print('Alpha: {}\n'.format(reg.alpha_))
print('Lambda: {}\n'.format(reg.lambda_))

'''
Data shape: (150, 4)

Labels shape: (150,)

Coefficients: array([-0.11174619, -0.03900476,  0.24330537,  0.57343721])

Intercept: 0.17022693722601356

R2: 0.9303454031271241

Alpha: 20.983865171760993

Lambda: 9.545491382343116
'''

print('------Ex: ------')


def bayes_ridge(data, labels):
    reg = linear_model.BayesianRidge()
    reg.fit(data, labels)
    return reg
