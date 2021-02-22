def alphabet_war(s):
    n = len(s)
    arr = [" "] * n
    count = 0
    shelter = ""
    for i, c in enumerate(s):
        if c == "[":
            shelter = "["
        elif shelter and c.isalpha():
            arr[i] = c
        elif c == "]":
            shelter = ""
        elif c == "#":
            count += 1
            arr[i] = " " + c + " "

    if not count:
        return s.replace("[", "").replace("]", "")

    s = "".join(arr).split()
    countHit = [0] * len(s)
    count = 0
    for i in range(len(s)):
        if s[i] == "#":
            count += 1
        else:
            countHit[i] = count
            count = 0
    count = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "#":
            count += 1
        else:
            countHit[i] += count
            count = 0

    res = ""
    for i, c in enumerate(s):
        if c != "#":
            if countHit[i] < 2:
                res += c

    return res


b = '[ab]adfd[dd]##[abe]dedf[ijk]d#d[h]#'
print(alphabet_war(b))
