def scoring_options_rec(n, result):
    if n < 0:
        return 0

    if result[n] > 0:
        return result[n]

    # Memoize
    result[n] = scoring_options_rec(n - 1, result) + \
                scoring_options_rec(n - 2, result) + \
                scoring_options_rec(n - 4, result)

    return result[n]


def scoring_options(n):
    if n <= 0:
        return 0

    result = [-1] * (n + 1)
    result[0] = 1

    scoring_options_rec(n, result);

    return result[n]


print("Number of ways score 5 can be reached = " + str(scoring_options(5)))
