import random
import numpy as np
from PythonNumpy.tools import timeit  # get time it from tools.py(custom module)


def add_python(Z1, Z2):
    return [z1 + z2 for (z1, z2) in zip(Z1, Z2)]


def add_numpy(Z1, Z2):
    return np.add(Z1, Z2)


Z1 = random.sample(range(1000), 100)
Z2 = random.sample(range(1000), 100)

timeit("add_python(Z1, Z2)", globals())
timeit("add_numpy(Z1, Z2)", globals())
