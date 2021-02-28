# https://www.codewars.com/kata/59d727d40e8c9dd2dd00009f
def balance(book: str):
    b = ""
    for i, c in enumerate(book):
        if c.isalnum() or c == "." or c == "\n":
            b += c
        else:
            b += " "
    arr = [_ for _ in b.splitlines() if _]
    total = float(arr[0])
    res = [f"Original Balance: {total:.2f}"]
    expense = 0
    for i in arr[1:]:
        a = i.split()
        checkID = a[0]
        category = a[1]
        amount = float(a[2])
        expense += amount
        res.append(f"{checkID} {category} {amount:.2f} Balance {total - amount:.2f}")
        total -= amount
    res.append(F"Total expense  {expense:.2f}")
    res.append(F"Average expense  {expense / (len(arr) - 1):.2f}")
    return "\r\n".join(res)


b1 = """1000.00!=
125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10
"""

b1sol = """Original Balance: 1000.00\r
125 Market 125.45 Balance 874.55\r
126 Hardware 34.95 Balance 839.60\r
127 Video 7.45 Balance 832.15\r
128 Book 14.32 Balance 817.83\r
129 Gasoline 16.10 Balance 801.73\r
Total expense  198.27\r
Average expense  39.65"""
print(balance(b1) == b1sol)
