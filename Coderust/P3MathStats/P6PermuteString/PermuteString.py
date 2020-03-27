result = []


def swap_char(input_string, i, j):
    # not optimal as we are constructing new string objects
    t = list(input_string)
    temp = t[i]
    t[i] = t[j]
    t[j] = temp
    return ''.join(t)


def permute_string_rec(input_string, current_index):
    if current_index is len(input_string) - 1:
        result.append(input_string)
        return

    for i in range(current_index, len(input_string)):
        swapped_input_string = swap_char(input_string, current_index, i);
        permute_string_rec(swapped_input_string,
                           current_index + 1);


def permute_string(input_string):
    permute_string_rec(input_string, 0)
    return result


input_string = "bad";
print("All permutations of " + input_string)
perms = permute_string(input_string)
for p in perms:
    print(p)
