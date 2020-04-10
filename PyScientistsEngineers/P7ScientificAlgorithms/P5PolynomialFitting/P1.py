import numpy as np

x = np.arange(-10, 11)
y = np.random.randn(len(x))  # generating random data for y
z = np.polyfit(x, y, 3)  # computing coeffiecients of polynomial of order 3
print(z)
# [-0.00292027 -0.0051181 0.11961561 0.21090914]
