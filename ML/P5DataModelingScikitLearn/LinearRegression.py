import numpy as np
import pandas as pd

print('------B. Basic linear regression------')
pizza_data = pd.DataFrame([[2100, 800],
                           [2500, 850],
                           [1800, 760],
                           [2000, 800],
                           [2300, 810]],
                          )

pizza_prices = pd.DataFrame([10.99, 12.5, 9.99, 10.99, 11.99])
print('{}\n'.format(repr(pizza_data)))
print('{}\n'.format(repr(pizza_prices)))
'''
array([[2100,  800],
       [2500,  850],
       [1800,  760],
       [2000,  800],
       [2300,  810]])

array([10.99, 12.5 ,  9.99, 10.99, 11.99])
'''

from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit(pizza_data, pizza_prices)

# new pizza data
new_pizzas = np.array([[2000, 820],
                       [2200, 830]])

price_predicts = reg.predict(new_pizzas)
print('{}\n'.format(repr(price_predicts)))
'''
array([10.86599206, 11.55111111])
'''

print('Coefficients: {}\n'.format(repr(reg.coef_)))
'''
Coefficients: array([0.00330913, 0.00232937])
'''
print('Intercept: {}\n'.format(reg.intercept_))
'''
Intercept: 2.3376587301587346
'''

# Using previously defined pizza_data, pizza_prices
r2 = reg.score(pizza_data, pizza_prices)
print('R2: {}\n'.format(r2))
'''
R2: 0.9758349388652625
'''

print('------Ex: ------')


def linear_reg(data, labels):
    reg = linear_model.LinearRegression()
    reg.fit(data, labels)
    return reg
