import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100)
y = x ** 2
fig = plt.figure(figsize=(10, 5), dpi=100)
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # add_axes([bottom x, bottom y, width, height])
ax1.plot(x, y, 'b')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Example figure')

plt.show()
