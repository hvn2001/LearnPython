import numpy as np
import pandas as pd

print('------B. Choosing the best alpha------')
pizza_data = pd.DataFrame([[2100, 800],
                           [2500, 850],
                           [1800, 760],
                           [2000, 800],
                           [2300, 810]],
                          )

pizza_prices = pd.DataFrame([10.99, 12.5, 9.99, 10.99, 11.99])

from sklearn import linear_model

reg = linear_model.Ridge(alpha=0.1)
reg.fit(pizza_data, pizza_prices)
print('Coefficients: {}\n'.format(repr(reg.coef_)))
print('Intercept: {}\n'.format(reg.intercept_))
r2 = reg.score(pizza_data, pizza_prices)
print('R2: {}\n'.format(r2))

'''
Coefficients: array([0.00330919, 0.0023288 ])

Intercept: 2.337978289647138

R2: 0.9758349388362841
'''

print('------B. using the RidgeCV object------')
from sklearn import linear_model

alphas = [0.1, 0.2, 0.3]
reg = linear_model.RidgeCV(alphas=alphas)
reg.fit(pizza_data, pizza_prices)
print('Coefficients: {}\n'.format(repr(reg.coef_)))
print('Intercept: {}\n'.format(reg.intercept_))
print('Chosen alpha: {}\n'.format(reg.alpha_))

'''
Coefficients: array([0.00330932, 0.00232767])

Intercept: 2.3386168534481815

Chosen alpha: 0.3
'''

print('------B. Ex------')
def cv_ridge_reg(data, labels, alphas):
  reg = linear_model.RidgeCV(alphas=alphas)
  reg.fit(data, labels)
  return reg

