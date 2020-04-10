from scipy import *
from scipy.integrate import quad, dblquad, tplquad


def f(phi, theta, r):
    return (r ** 2 * sin(theta))


# call dblquad to integrate the function f
# r goes from 0 to 3
# theta goes from 0 to pi
# phi goes from 0 to 2pi

val, err = tplquad(f, 0, 3, lambda r: 0, lambda r: pi, lambda r, theta: 0, lambda r, theta: 2 * pi)

print("Actual Volume:", (pi) * (3 ** 3) * (4 / 3))  # computed by formula
print("Value of integral:", val)
print("Error in integral:", err)
