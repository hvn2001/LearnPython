import scipy as sc
import matplotlib.pyplot as plt

x = sc.arange(0, 2 * sc.pi, 0.1)
y = sc.sin(x)

plt.plot(x, y)

plt.show()  # I add
