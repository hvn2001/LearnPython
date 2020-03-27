import re


def regx_match_rec(text, pattern):
    if not text and not pattern:
        return True

    if text and not pattern:
        return False

    if len(pattern) > 1 and pattern[1] == '*':

        remaining_pattern = pattern[2:]
        remaining_text = text

        for i in range(0, len(text) + 1):

            if regx_match_rec(remaining_text, remaining_pattern):
                return True

            if not remaining_text:
                return False

            if pattern[0] != '.' and remaining_text[0] != pattern[0]:
                return False

            remaining_text = remaining_text[1:]

    if not text or not pattern:
        return False

    if pattern[0] == '.' or pattern[0] == text[0]:
        remaining_text = ""
        if len(text) >= 2:
            remaining_text = text[1:]

        remaining_pattern = ""
        if len(pattern) >= 2:
            remaining_pattern = pattern[1:]

        return regx_match_rec(remaining_text, remaining_pattern)

    return False


def regx_match(text, pattern):
    return regx_match_rec(text, pattern)


s = "fabbbc"
p = ".ab*c"
output = regx_match(s, p)

pt = re.compile(p)

output3 = False
m = pt.match(s)
if m and m.end() == len(s):
    output3 = True

if output == True:
    print(s, p, end=" ")
    print("match")

else:
    print(s, p, end=" ")
    print("did not match.")

assert output == output3
