def fixed_xor(a, b):
    res = "".join(F'{int(x, 16) ^ int(y, 16):x}' for x, y in zip(a, b))
    return res
    # if not a or not b: return ""
    # aLen, bLen = len(a), len(b)
    # a = a[:min(aLen, bLen)]
    # b = b[:min(aLen, bLen)]
    # aNum = int(a, 16)
    # bNum = int(b, 16)
    # return hex(aNum ^ bNum)[2:].zfill(min(aLen, bLen))


a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"
# a = "aadf"
# b = "bce2"
d = fixed_xor(a, b)
c = "746865206b696420646f6e277420706c6179"
# c = "163d"
print(c == d)
