import numpy as np
import matplotlib.pyplot as plt

n = 3  # polynomial order
x = np.linspace(-10, 11, 20)
y = 0.5 * np.random.randn(len(x)) + (0.1 * x ** 2)  # generating random data for y
z = np.polyfit(x, y, n)  # computing coeffiecients of polynomial of order 3

p = np.poly1d(z)  # generating a polynomial from the coefficients
xp = np.linspace(-10, 11, 100)  # generating xdata for polynomial plotting

fig, ax = plt.subplots()
ax.plot(x, y, 's', marker='.')  # plotting actual data
ax.plot(xp, p(xp))  # plotting polynomial data

plt.show()  # I add
