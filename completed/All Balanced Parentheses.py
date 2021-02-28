# https://www.codewars.com/kata/5426d7a2c2c7784365000783/train/python
def balanced_parens(n):
    res = []

    def dfs(l, r, curP):
        if l == r == n:
            res.append(curP)
            return
        l < n and dfs(l + 1, r, curP + "(")
        r < l and dfs(l, r + 1, curP + ")")

    dfs(0, 0, "")
    return res


print(balanced_parens(3))
