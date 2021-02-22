d = {chr(ord('A') + i - 1): i for i in range(1, 27)}


def find_the_key(message, code):
    arr = "".join(map(str, [code[i] - d[message[i].upper()] for i in range(len(code))]))
    n = len(arr)
    res = arr
    for i in range(1, n):
        x = n // (i)
        m = n % i
        if arr[:i] * x == arr[:i * x] and arr[:m] == arr[i * x:]:
            res = arr[:i]
            break

    return int(res)


message = "scout"
code = [20, 12, 18, 30, 22]
print(find_the_key(message, code))
