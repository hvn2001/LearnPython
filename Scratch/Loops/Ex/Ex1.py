def check_balance(brackets):  # The argument is a string
    count = 0
    for c in brackets:
        if c == '[':
            count += 1
        elif c == ']':
            count -= 1
        if count < 0:
            return False
    return count == 0


print(check_balance("[[[[][]]]]"))
