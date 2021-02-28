# https://www.codewars.com/kata/546d15cebed2e10334000ed9/train/python
def solve_runes(exp: str):
    ops = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y}
    exist = {int(s) for s in exp if s.isdigit()}
    left, right = exp.split("=")

    def checkZero(s: str):
        if len(s) < 2: return True
        if s[0] in "-?":
            if s[1] == "?": return False
        return True

    if not checkZero(left) or not checkZero(right):
        exist.add(0)

    opID = 0
    for i in range(1, len(left)):
        if left[i] in "+-*":
            opID = i
            break

    a, b, c = left[:opID], left[opID + 1:], right
    op = left[opID]

    for i in range(0, 10):
        if i not in exist:
            A, B, C = a.replace("?", str(i)), b.replace("?", str(i)), c.replace("?", str(i)),
            if ops[op](int(A), int(B)) == int(C):
                return i

    return -1


# exp = "??*??=302?"
exp = "?*123?45=?"
print(solve_runes(exp))
