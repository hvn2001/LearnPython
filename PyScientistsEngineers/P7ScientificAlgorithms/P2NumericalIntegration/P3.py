from scipy import *
from scipy.integrate import quad, dblquad


def f(y, x):
    return x ** 2 * y


# call dblquad to integrate the function f
# x goes from 0 to 3
# y goes from 0 to 2
val, err = dblquad(f, 0, 3, lambda x: 0, lambda x: 2)

print("Actual Value:", 18)  # calculated by hand
print("Value of integral:", val)
print("Error in integral:", err)
