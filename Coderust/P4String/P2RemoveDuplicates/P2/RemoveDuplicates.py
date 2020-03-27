# this solution does not require any extra memory
# but runs in O(n^2) time

# Null terminating strings are not used in Python.
# For this question, assume that you are passed a
# null terminated string (array of characters).
from array import array


def remove_duplicates(str_arr):
    write_index = 0

    for i in range(len(str_arr)):
        found = False

        for j in range(0, write_index):
            if str_arr[i] == str_arr[j]:
                found = True
                break

        if found == False:
            str_arr[write_index] = str_arr[i]
            write_index += 1

    if write_index != len(str_arr):
        str_arr[write_index] = '\0'


def get_array(t):
    s = array('u', t)
    return s


def print_array(s):
    i = 0
    result = ""
    while i < len(s) and s[i] != '\0':
        result += s[i]
        i += 1
    print(result)


def are_equal(s1, s2):
    if s1 == None and s2 == None:
        return True

    if s1 == None or s2 == None:
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


s = "dabbac"
print("Before: " + str(s))
temp1 = get_array(s)
remove_duplicates(temp1)
print("After: ", end="")
print_array(temp1)
