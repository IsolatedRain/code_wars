def missing(s):
    n = len(s) // 2

    def isValid(a: str):
        b = str(int(a) + 1)
        idx = 0
        while idx < len(s):
            if not s[idx:].startswith(a):
                if not s[idx:].startswith(b):
                    return False
                idx += len(b)
            else:
                idx += len(a)
            a = b
            b = str(int(b) + 1)
        return True

    firNum = ""
    for i in range(1, n+1):
        if isValid(s[:i]):
            firNum = s[:i]
            break

    if not firNum: return  -1
    i = 0
    curNum = firNum
    while i < len(s):
        if curNum != s[i:i + len(curNum)]:
            return int(curNum)
        i += len(curNum)
        curNum = str(int(curNum) + 1)

    return -1


# s = "998999100010011003"
s = "123567"
print(missing(s))
