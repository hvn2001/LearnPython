from scipy import *
from scipy.interpolate import *
import matplotlib.pyplot as plt


def f(x):  # function for signal
    return (5 * sin(x)) + (0.1 * x ** 2) + (0.01 * x ** 3)


n = 10
x = linspace(-2 * pi, 2 * pi, n)  # generating xdata
noise = randn(n)  # generating random noise
y = f(x) + noise  # adding noise to the signal

# plotting signal
fig, ax = plt.subplots()
ax.plot(x, y, 's', marker='.')  # the third argument creates a scatter plot
ax.set_title('Signal')

plt.show()  # I add
