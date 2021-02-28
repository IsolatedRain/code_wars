def remove_parentheses(s):
    res = ""
    leftP = 0
    d = {"(": 1, ")": -1}
    for i, c in enumerate(s):
        if c not in "()":
            if not leftP: res += c
        else:
            leftP += d[c]
    return res


# s = "(first group) (second group) (third group)"
s = "a(b(c))"
print(remove_parentheses(s))
