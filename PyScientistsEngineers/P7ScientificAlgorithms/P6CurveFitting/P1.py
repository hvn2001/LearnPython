from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def RMSE(y1, y2):
    return (np.square(np.subtract(y1, y2))).mean()


def func(x, A, a, b):
    y = A * np.exp(a * x) + b
    return y


x = np.linspace(0, 4, 50)
y = 0.2 * np.random.randn(len(x)) + func(x, 4.5, -1.3, 3)  # adding noise to signal

popt, pcov = curve_fit(func, x, y, p0=(3, -1, 2.9))  # p0 are initial estimates
print("A = ", popt[0], "a = ", popt[1], "b = ", popt[2])
yfit = func(x, *popt)  # equivalent to popt[0], popt[1], popt[2]
plt.figure()
plt.plot(x, y, 'bo', label='observed')
plt.plot(x, yfit, 'r', label='fit')
plt.legend(loc='best')

rmse = RMSE(y, yfit)
plt.title('RMSE: ' + str(rmse));

# A =  4.533629312391205 a =  -1.302682903177926 b =  3.04363073491686
plt.show()  # I add
