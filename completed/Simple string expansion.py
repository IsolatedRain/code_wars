def solve(st):
    def dfs(curS):
        alp = ""
        for i, c in enumerate(curS):
            if c.isalpha():
                alp += c
            elif c.isdigit():
                return alp + dfs(curS[i + 1:]) * int(c)
            elif c == ")":
                return alp

    return dfs(st)


print(solve("k(a3(b(a2(c))))") == "kabaccbaccbacc")
