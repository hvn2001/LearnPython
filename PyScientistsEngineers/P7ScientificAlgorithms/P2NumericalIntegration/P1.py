from scipy import *
from scipy.integrate import quad


# function to be integrated
def f(x):
    return (2 * sin(x) * cos(x))


# call quad to integrate the function f from 0 to pi/2
val, err = quad(f, 0, pi / 2)
print("Value of integral:", val)
print("Error in integral:", err)
'''
Value of integral: 0.9999999999999999
Error in integral: 1.1102230246251564e-14
'''
