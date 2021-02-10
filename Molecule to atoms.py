import collections


def parse_molecule(s: str):
    s = "(" + s + ")"
    L, R = 1, 1
    arr = []
    while R < len(s):
        if s[R] in {"{", "}", "(", ")", "[", "]"} or s[R].isupper() or s[R].isdigit():
            arr.append(s[L:R])
            L = R

        R += 1
    arr = arr[1:]
    for i, v in enumerate(arr):
        if i > 0 and arr[i].isdigit() and arr[i - 1].isdigit():
            arr[i - 1:i + 1] = [arr[i - 1] + arr[i]]
    idx = 0
    while idx < len(arr):
        if arr[idx].isalpha() and idx < len(arr) - 1 and not arr[idx + 1].isdigit():
            arr[idx:idx + 1] = [arr[idx], "1"]
            idx += 1
        if arr[idx] in "}])" and idx < len(arr) - 1 and not arr[idx + 1].isdigit():
            arr[idx:idx + 1] = [arr[idx], "1"]
            idx += 1
        idx += 1
    stack = []
    i = 0
    if not arr[-1].isdigit():
        arr.append("1")

    while i < len(arr):
        c = arr[i]
        if c in ")}]":
            cur = []
            n = 1 if i == len(arr) - 1 else int(arr[i + 1])
            while stack and stack[-1] not in "{[(":
                cur.append(stack.pop())
            stack.pop()
            for j in range(len(cur)):
                if cur[j].isdigit():
                    cur[j] = str(int(cur[j]) * n)
            for j in range(len(cur) - 1, -1, -1):
                stack.append(cur[j])
            i += 1
        else:
            stack.append(c)
        i += 1
    d = collections.defaultdict(int)
    for i in range(0, len(stack), 2):
        d[stack[i]] += int(stack[i + 1])
    return d


formula = 'K4[FeN(SO3)2]2'
# formula = "H2O"
# formula = "C6H12O6"
print(parse_molecule(formula))
