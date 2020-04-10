from scipy import *
from scipy.interpolate import *
import matplotlib.pyplot as plt


def f(x):  # function for signal
    return (5 * sin(x)) + (0.1 * x ** 2) + (0.01 * x ** 3)


n = 10
x = linspace(-2 * pi, 2 * pi, n)  # generating xdata
noise = randn(n)  # generating random noise
y = f(x) + noise  # adding noise to the signal

x_plotter = linspace(-2 * pi, 2 * pi, 100)
y0 = interp1d(x, y, kind='linear')  # interpolation of type linear
y1 = interp1d(x, y, kind='quadratic')  # interpolation of type quadratic

# plotting the signal and interpolations
fig, ax = plt.subplots()

ax.plot(x, y, 's', marker='o', color='k', label='Noisy Data')  # signal
ax.plot(x_plotter, y0(x_plotter), label='linear')
ax.plot(x_plotter, y1(x_plotter), label='quadratic')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Interpolation')

fig.tight_layout()
plt.show()  # I add
