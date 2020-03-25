import pandas as pd

print('------A. Sparse regularization------')
data = pd.DataFrame([[2100, 800],
                     [2500, 850],
                     [1800, 760],
                     [2000, 800],
                     [2300, 810]],
                    )
labels = pd.DataFrame([10.99, 12.5, 9.99, 10.99, 11.99])

print('Data shape: {}\n'.format(data.shape))
print('Labels shape: {}\n'.format(labels.shape))

from sklearn import linear_model

reg = linear_model.Lasso(alpha=0.1)
reg.fit(data, labels)
print('Coefficients: {}\n'.format(repr(reg.coef_)))
print('Intercept: {}\n'.format(reg.intercept_))
print('R2: {}\n'.format(reg.score(data, labels)))
''' Educa
Data shape: (150, 4)

Labels shape: (150,)

Coefficients: array([ 0.        , -0.        ,  0.40830957,  0.        ])

Intercept: -0.534699558318563

R2: 0.895831189504504
'''

print('------Ex: ------')


def lasso_reg(data, labels, alpha):
    reg = linear_model.Lasso(alpha=alpha)
    reg.fit(data, labels)
    return reg
