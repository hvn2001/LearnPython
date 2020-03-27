# this solution uses extra memory
# to keep all characters present in string.

# Null terminating strings are not used in Python.
# For this question, assume that you are passed a
# null terminated string (array of characters).
from array import array


def remove_duplicates(s):
    hashset = set([])
    write_index = 0
    read_index = 0

    while read_index < len(s):
        if s[read_index] not in hashset:
            hashset.add(s[read_index])
            s[write_index] = s[read_index]
            write_index += 1

        read_index += 1

    s[write_index] = '\0'


def getArray(t):
    s = array('u', t)
    return s


def print_array(s):
    i = 0
    result = ""
    while s[i] != '\0':
        result += s[i]
        i += 1
    print(result)


def are_equal(s1, s2):
    if s1 is None and s2 is None:
        return True

    if s1 is None or s2 is None:
        return False

    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == '\0' and s2[j] == '\0':
            return True

        if s1[i] != s2[j]:
            return False

        i += 1
        j += 1

    return False


# Test Program.

s = "dabbac"
print("Before: " + s)
temp1 = getArray(s)
remove_duplicates(temp1)
print("After: ", end="")
print_array(temp1)
