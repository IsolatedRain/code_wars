def increment_string(s: str):
    digit = s[(len(s.rstrip("0123456789"))):]
    if not digit: return s + "1"
    v = str(int(digit) + 1).zfill(len(digit))
    if len(digit) == len(s):
        return v
    return s[:len(s) - len(digit)] + v


word = "foo"
# word = "foobar001"
# word = "009"
# word = "8129461190440702"
print(increment_string(word))
