from scipy import *
from scipy.integrate import quad

# call quad to integrate the function f from -Inf to Inf
val, err = quad(lambda x: exp(-x ** 2), -Inf, Inf)
print("Value of integral:", val)
print("Error in integral:", err)
