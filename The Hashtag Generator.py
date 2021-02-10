def generate_hashtag(s):
    s = s.strip()
    if not s: return False
    words = s.split()
    res = "#"
    for w in words:
        res += w.capitalize()
    return res if len(res) < 150 else False


words = '    codewars      is Nice    '
print(generate_hashtag(words))
