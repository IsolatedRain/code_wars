def reverse_in_parentheses(s: str):
    s = list(s)
    leftPIndex = []
    d = {"(": ")", ")": "("}

    def reverse(arr: list):
        L, R = 0, len(arr) - 1
        while L < R:
            arr[R], arr[L] = arr[L], arr[R]
            L += 1
            R -= 1
        for i, c in enumerate(arr):
            if c in "()":
                arr[i] = d[c]
        return arr

    for i, c in enumerate(s):
        if c == "(":
            leftPIndex.append(i)
        elif c == ")":
            L = leftPIndex.pop()
            s[L:i + 1] = reverse(s[L:i + 1])

    res = "".join(s)
    return res


# print(reverse_in_parentheses("h(el)lo") == "h(le)lo")
print(reverse_in_parentheses("a ((d e) c b)") == "a (b c (d e))")
