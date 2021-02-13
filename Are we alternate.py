def is_alt(s):
    vowels = {*"aeiou"}
    t = ""
    for i in s:
        if i in vowels:
            t += "0"
        else:
            t += "1"

    if "00" in t or "11" in t:
        return False

    return True


s = "banana"
print(is_alt(s))
