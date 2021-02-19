def integer_right_triangles(p):
    n = p // 2 + 1
    res = []
    for a in range(1, n):
        for b in range(a, n):
            c = p - a - b
            if c <= a or c <= b: break
            if a ** 2 + b ** 2 == c ** 2:
                res.append([a, b, c])
    return res


# p = 1000
# p = 1000000
p = 70
print(integer_right_triangles(p))
