import itertools as it
from PythonNumpy.tools import timeit


def solution_2():
    # Itertools
    # 14641 (=11*11*11*11) iterations & tests
    return [(i, j, k, l)
            for i, j, k, l in it.product(range(11), repeat=4) if i + j + k + l == 10]


timeit("solution_2()", globals())
