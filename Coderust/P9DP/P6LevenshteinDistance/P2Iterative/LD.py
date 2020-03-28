def minimum(a, b, c):
    return min(a, b, c)


def levenshtein_distance(str1, str2):  # degenerate cases
    if (str1 == str2):
        return 0

    if (len(str1) == 0):
        return len(str2)

    if (len(str2) == 0):
        return len(str1)

    # for all i and j, d[i, j] will hold the Levenshtein distance between
    # the first i characters of str1 and the first j characters of str2;
    # note that d has(m + 1) * (n + 1) values
    d = []
    for i in range(len(str1) + 1):
        d.append([])
        for j in range(len(str2) + 1):
            d[i].append(0)

    # source prefixes can be transformed into empty string by# dropping all characters
    for i in range(0, len(str1) + 1):
        d[i][0] = i

    # target prefixes can be reached from empty source prefix# by inserting every character
    for j in range(1, len(str2) + 1):
        d[0][j] = j

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0  # no operation required
            else:
                cost = 1

            d[i][j] = minimum(
                d[i - 1][j] + 1,  # a deletion
                d[i][j - 1] + 1,  # an insertion
                d[i - 1][j - 1] + cost)  # a substitution

    return d[len(str1)][len(str2)]


str1 = "kitten";
str2 = "sitting";
ld = levenshtein_distance(str1, str2);
print("LD(" + str1 + ", " + str2 + ") = " + str(ld));
