# https://www.codewars.com/kata/58e24788e24ddee28e000053/train/python
import collections


def simple_assembler(p):
    d = collections.defaultdict(int)
    arr = [_.split() for _ in p]
    n = len(arr)
    i = 0
    while i < n:
        if arr[i][0] == "mov":
            d[arr[i][1]] = d[arr[i][2]] if arr[i][2].isalpha() else int(arr[i][2])
        elif arr[i][0] == "dec":
            d[arr[i][1]] -= 1
        elif arr[i][0] == "inc":
            d[arr[i][1]] += 1
        else:
            if arr[i][1] == "0":
                i += 1
                continue
            if arr[i][1].isalpha() and not d[arr[i][1]]:
                i += 1
                continue
            i += d[arr[i][2]] if arr[i][2].isalpha() else int(arr[i][2])
            continue
        i += 1
    return d


# code = '''\
# mov a 5
# inc a
# dec a
# dec a
# jnz a -1
# inc a'''
# code = code.splitlines()
# code = ['mov a -10', 'mov b a', 'inc a', 'dec b', 'jnz a -2']
# code = ['mov u 35', 'mov n 21', 'mov q 20', 'mov z 1', 'jnz z 4', 'jnz u 3', 'inc u', 'dec u', 'inc u', 'dec u',
#         'inc u', 'dec n', 'inc n', 'inc n', 'inc n', 'dec q', 'inc q']
# code = ['mov a 5', 'inc a', 'dec a', 'dec a', 'jnz a -1', 'inc a']
code = ['mov a 1', 'mov b 1', 'mov c 0', 'mov d 26', 'jnz c 2', 'jnz 1 5', 'mov c 7', 'inc d', 'dec c', 'jnz c -2',
        'mov c a', 'inc a', 'dec b', 'jnz b -2', 'mov b c', 'dec d', 'jnz d -6', 'mov c 18', 'mov d 11', 'inc a',
        'dec d', 'jnz d -2', 'dec c', 'jnz c -5']
print(simple_assembler(code))
