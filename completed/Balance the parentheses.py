def fix_parentheses(s):
    stack = []
    R = ""
    for i, c in enumerate(s):
        if c == "(":
            stack.append(")")
        else:
            if not stack:
                R += "("
            else:
                stack.pop()
    L = len(stack) * ")"
    return R + s + L


# print(fix_parentheses('))))(()(') == '(((())))(()())')
print(fix_parentheses('()()))()())') == '(((()()))()())')
