def smallest(n):
    s = list(str(n))

    def swap(i, p):
        t = s[:]
        t.insert(i, t.pop(p))
        return int(''.join(t))

    return min([swap(i, p), p, i] for i in range(len(s)) for p in range(len(s)))


# a = smallest(261235)
# b = [126235, 2, 0]
# print(smallest(29917))
# print(smallest(187863002809))
b = smallest(935855753)
a = [358557539, 0, 8]
print(b)
print(a)
# b = smallest(900609234202395093)
# a = [6092342023950939, 0, 17]
# b = smallest(40012573172971286)
# a = [124573172971286, 0, 4]
# b = smallest(261235)
# b = smallest(908293892600719479)
# a = [82938926007194799, 0, 16]
# b = smallest(517929265684664725)
# a = [157929265684664725, 0, 1]
# def smallest(n):
#     print(n)
#     s = list(str(n))
#     numsID = {}
#     for i, c in enumerate(s):
#         numsID[c] = i
#     i1, s1 = len(s) - 1, len(s) - 1
#     checked = set()
#     for i, c in enumerate(s):
#         getIS = False
#         if c not in checked:
#             checked.add(c)
#             for j in range(int(c)):
#                 if str(j) in numsID and numsID[str(j)] > i:
#                     getIS = True
#                     i1 = i
#                     s1 = numsID[str(j)]
#                     break
#         if getIS: break
#
#     for i in range(i1 - 1, -1, -1):
#         if s[i] == s[i1]:
#             i1 = i
#         else:
#             break
#     for i in range(i1 - 1, -1, -1):
#         if s[i] == s[s1]:
#             i1 = i
#         else:
#             break
#     for i in range(s1 - 1, -1, -1):
#         if s[i] == s[s1]:
#             s1 = i
#         else:
#             break
#
#     num1 = int("".join(s[:i1]) + s[s1] + "".join(s[i1:s1]) + "".join(s[s1 + 1:]))
#     bigNumID = len(s) - 1
#     for i in range(len(s) - 1, -1, -1):
#         if s[i] >= s[bigNumID]:
#             bigNumID = i
#     num2 = int("".join(s[:bigNumID] + s[bigNumID + 1:]) + s[bigNumID])
#
#     num3, i3, s3 = n, len(s) - 1, len(s) - 1
#     if s[1] == "0":
#         for i in range(2, len(s)):
#             if s[i] > s[0]:
#                 num3 = int("".join(s[1:i]) + s[0] + "".join(s[i:]))
#                 i3, s3 = i - 1, 0
#                 break
#     num4, i4, s4 = n, len(s) - 1, len(s) - 1
#     if s[0] > s[1]:
#         for i in range(2, len(s)):
#             if s[i] >= s[0]:
#                 num4 = int("".join(s[1:i]) + s[0] + "".join(s[i:]))
#                 i4, s4 = i - 1, 0
#     minNum = min(num1, num2, num3, num4)
#     if num4 == minNum:
#         return [num4, s4, i4]
#     if num3 == minNum:
#         return [num3, s3, i3]
#     if num2 == minNum:
#         i3 = len(s) - 1
#         for i in range(len(s) - 1, -1, -1):
#             if s[i] == s[bigNumID]:
#                 i3 = i - 1
#             else:
#                 break
#         return [num2, bigNumID, i3]
#     if s1 == 1 and i1 == 0:
#         return [num1, i1, s1]
#     return [num1, s1, i1]
