def is_formation_possible(lst, word):
    if len(word) < 2 or len(lst) < 2:
        return False
    # Create Trie and insert dictionary elements in it
    hash_table = dict()
    for elem in lst:
        hash_table[elem] = True

    for i in range(1, len(word)):
        # Slice the word into two strings in each iteration
        first = word[0:i]
        second = word[i:len(word)]
        check1 = False
        check2 = False

        try:
            check1 = hash_table[first]
        except KeyError:
            check1 = False

        try:
            check2 = hash_table[second]
        except KeyError:
            check2 = False

        # Return True If both substrings are present in the trie
        if check1 and check2:
            return True

    return False


keys = ["the", "hello", "there", "answer",
        "any", "educative", "world", "their", "abc"]
print(is_formation_possible(keys, "helloworld"))
