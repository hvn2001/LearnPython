import numpy as np
import matplotlib.pyplot as plt


# function to compute root mean square error
def RMSE(y1, y2):
    return (np.square(np.subtract(y1, y2))).mean()


n = 0  # polynomial order
x = np.linspace(-5, 5, 40)


def create(x):  # I add
    return np.random.randn(len(x))


y = create(x)  # create random data

z = np.polyfit(x, y, n)  # computing coeffiecients of polynomial of order n

p = np.poly1d(z)  # generating a polynomial from the coefficients
xp = np.linspace(-5, 5, 100)  # generating xdata for polynomial plotting

error = RMSE(y, p(x))  # computing error
print("Root mean square error:", error)

fig, ax = plt.subplots()
ax.plot(x, y, 's', marker='.')  # plotting actual data
ax.plot(xp, p(xp))  # plotting polynomial data

plt.show()  # I add
# Origin: Root mean square error: 10486.434215237148
