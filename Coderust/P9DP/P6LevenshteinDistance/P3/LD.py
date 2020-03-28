def minimum(a, b, c):
    return min(a, b, c)


def levenshtein_distance(str1, str2):
    # degenerate cases
    if str1 == str2:
        return 0

    if len(str1) == 0:
        return len(str2)

    if len(str2) == 0:
        return len(str1)

    # create two work arrays of integer distances
    d1 = []
    d2 = []

    for i in range(len(str2) + 1):
        d1.append(0)

    for i in range(len(str2) + 1):
        d2.append(0)

    # initialize d1 (the previous row of distances)
    # this row is A[0][i]: edit distance for an empty str1
    # the distance is just the number of characters to delete from str2
    for i in range(0, len(str2) + 1):
        d1[i] = i

    for i in range(0, len(str1)):
        # calculate d2 (current row distances) from the previous row d1

        # first element of d2 is A[i+1][0]
        # edit distance is delete (i+1) chars from str1 to match empty str2
        d2[0] = i + 1

        # use formula to fill in the rest of the row
        for j in range(0, len(str2)):
            if (str1[i] == str2[j]):
                cost = 0
            else:
                cost = 1

            d2[j + 1] = minimum(d2[j] + 1, d1[j + 1] + 1, d1[j] + cost)

        # copy d2(current row) to d1(previous row) for next iteration
        for j in range(0, len(str2) + 1):
            d1[j] = d2[j]

    return d2[len(str2)]


str1 = "kitten"
str2 = "sitting"
ld = levenshtein_distance(str1, str2)
print("LD(" + str1 + ", " + str2 + ") = " + str(ld))
