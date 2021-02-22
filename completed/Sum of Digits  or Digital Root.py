def digital_root(n):
    # s = str(n)
    # while len(s) > 1:
    #     s = str(sum(map(int, list(s))))
    # return int(s)
    return n % 9 or n and 9


n = 132189
print(digital_root(0))
