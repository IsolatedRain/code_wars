import codecs


def encrypter(s):
    arr = codecs.encode(s, "rot13")
    a = "".join(chr(i) for i in range(ord("a"), ord("z") + 1))
    d = {i: j for i, j in zip(a, a[::-1])}
    return "".join(d[c] if c.isalpha() else c for c in arr)


print(encrypter("welcome to the organization") == "qibkyai ty tfi yvgmzenmteyz")
