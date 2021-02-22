def last_digit(n1, n2):
    if not n2: return 1
    n = n1 % 10
    curN = n
    lastDigits = [n]
    mod = 1
    # 尾数 不断 自乘， 会进入循环。
    # 求出该 循环， 检查 指数取余后,即 指数循环N次后， 会落在第几位。
    for i in range(1, 10):
        curN *= n
        curN %= 10
        if curN % 10 in lastDigits:
            mod = i
            break
        lastDigits.append(curN % 10)
    return lastDigits[n2 % mod - 1]


# n1 = 9
# n2 = 7
n1 = 3715290469715693021198967285016729344580685479654510946723
n2 = 68819615221552997273737174557165657483427362207517952651
print(last_digit(n1, n2))
