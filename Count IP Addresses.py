def ips_between(start, end):
    ip1, ip2 = start.split("."), end.split(".")
    res = 0
    curCarry = 1
    for i in range(3, -1, -1):
        res += curCarry * (int(ip2[i]) - int(ip1[i]))
        curCarry *= 256
    return res


print(ips_between("20.0.0.10", "20.0.1.0") == 246)
