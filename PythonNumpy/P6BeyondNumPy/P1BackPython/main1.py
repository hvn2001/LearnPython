from PythonNumpy.tools import timeit


def solution_1():
    # Brute force
    # 14641 (=11*11*11*11) iterations & tests
    Z = []
    for i in range(11):
        for j in range(11):
            for k in range(11):
                for l in range(11):
                    if i + j + k + l == 10:
                        Z.append((i, j, k, l))
    return Z


timeit("solution_1()", globals())
