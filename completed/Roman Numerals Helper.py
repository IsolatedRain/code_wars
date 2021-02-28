class RomanNumeralsHelper():
    def __init__(self):
        self.digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                       (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        self.roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def to_roman(self, n: int) -> str:
        res = []
        for digit, romanNum in self.digits:
            if not n: break
            count, n = divmod(n, digit)
            res.append(romanNum * count)
        return "".join(res)

    def from_roman(self, r: str) -> int:
        res = self.roman[r[-1]]
        for i in range(len(r) - 1):
            if self.roman[r[i]] < self.roman[r[i + 1]]:
                res -= self.roman[r[i]]
            else:
                res += self.roman[r[i]]
        return res
