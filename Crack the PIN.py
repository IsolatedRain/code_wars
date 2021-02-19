# don't print anything in the console, because it will take to much time
import hashlib


def crack(hash):
    res = ""
    for i in range(100000):
        m = hashlib.md5()
        cur = str(i).zfill(5)
        m.update(cur.encode("utf-8"))
        if m.hexdigest() == hash:
            return cur
    return res


print(crack("86aa400b65433b608a9db30070ec60cd"))
