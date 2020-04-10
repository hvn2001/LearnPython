def solution_3():
    # Author: Nick Poplas
    # Intricated iterations
    # 486 iterations, no test
    return [(a, b, c, (10 - a - b - c))
            for a in range(11) for b in range(11 - a) for c in range(11 - a - b)]


def solution_3_bis():
    # Iterator using intricated iterations
    # 486 iterations, no test
    return ((a, b, c, (10 - a - b - c))
            for a in range(11) for b in range(11 - a) for c in range(11 - a - b))


print(type(solution_3()))
# <class 'list'>
print(type(solution_3_bis()))
# <class 'generator'>
