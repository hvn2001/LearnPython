import numpy as np
from PythonNumpy.tools import timeit  # get time it from tools.py(custom module)


def test(X, Y):
    timeit("Z=X + 2.0*Y", globals())  # time taken by Z=X + 2.0*Y
    timeit("Z = X + 2*Y", globals())  # time taken by Z=X + 2*Y
    timeit("np.add(X, Y, out=X); np.add(X, Y, out=X)", globals())
    # time taken by np.add(X, Y, out=X); np.add(X, Y, out=X)


X = np.ones(100000000, dtype=np.int)
Y = np.ones(100000000, dtype=np.int)
test(X, Y)
