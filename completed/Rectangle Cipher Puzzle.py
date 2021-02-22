def cipher(phrase: str):
    n = len(phrase)
    a = 'this will probably not be fun'
    b = "tiks zjop twrggfrf uwz kl pcx"
    res = []
    t = []
    for i in range(n):
        if a[i] == " ":
            res.append("   ")
            t.append(" ")
            continue
        res.append((ord(b[i]) - ord(a[i]), i))
        t.append(ord(b[i]) + ord(a[i]) - 2 * ord("a"))
    print(res)
    print(t)
    return res


print(cipher('this will probably not be fun') == 'tiks zjop twrggfrf uwz kl pcx')
