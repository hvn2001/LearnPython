class STATE:
    START, INTEGER, DECIMAL, UNKNOWN, AFTER_DECIMAL = range(5)


def get_next_state(current_state, ch):
    if (current_state is STATE.START or
            current_state is STATE.INTEGER):
        if ch == '.':
            return STATE.DECIMAL
        elif ch >= '0' and ch <= '9':
            return STATE.INTEGER
        else:
            return STATE.UNKNOWN

    if current_state is STATE.DECIMAL:
        if ch >= '0' and ch <= '9':
            return STATE.AFTER_DECIMAL
        else:
            return STATE.UNKNOWN

    if current_state is STATE.AFTER_DECIMAL:
        if ch >= '0' and ch <= '9':
            return STATE.AFTER_DECIMAL
        else:
            return STATE.UNKNOWN
    return STATE.UNKNOWN


def is_number_valid(s):
    if not s:
        return True

    i = 0
    if s[i] == '+' or s[i] == '-':
        i = i + 1

    current_state = STATE.START

    for c in s[i:]:
        current_state = get_next_state(current_state, c)
        if current_state is STATE.UNKNOWN:
            return False
        i = i + 1

    if current_state is STATE.DECIMAL:
        return False;

    return True


print("Is the number valid 4.325? ", is_number_valid("4.325"))
print("Is the number valid 1.1.1? ", is_number_valid("1.1.1"))
print("Is the number valid 222? ", is_number_valid("222"))
print("Is the number valid 22.? ", is_number_valid("22."))
print("Is the number valid 0.1? ", is_number_valid("0.1"))
print("Is the number valid 22.22.? ", is_number_valid("22.22."))
print("Is the number valid 1.? ", is_number_valid("1."))
