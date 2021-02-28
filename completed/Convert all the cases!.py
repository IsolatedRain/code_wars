# https://www.codewars.com/kata/59be8c08bf10a49a240000b1/solutions/python
def change_case(identifier, targetCase):
    if not identifier: return ""

    def change2camel(s: str):
        words = s.replace("-", " ").replace("_", " ").split()
        return words[0] + "".join(i.capitalize() for i in words[1:])

    def change2snake(s: str):
        if "-" in s:
            return s.replace("-", "_")
        return "".join("_" + i.lower() if i.isupper() else i for i in s)

    def change2kebab(s: str):
        if "_" in s:
            return s.replace("_", "-")
        return "".join("-" + i.lower() if i.isupper() else i for i in s)

    def checkInput(s: str):
        ke = "-" in s
        sn = "_" in s
        for c in s:
            if not c.isalpha() and c not in "_-": return False
            if c.isupper() and (ke or sn): return False
        if ke and sn: return False
        return True

    if not checkInput(identifier) or not checkInput(targetCase): return None

    d = {"camel": change2camel, "snake": change2snake, "kebab": change2kebab}
    return d[targetCase](identifier)


# print(change_case("some-lisp-name", "camel"), "someLispName", "kebab-case to camelCase conversion should work")
# print(change_case("", "camel"))
# print(change_case("valid-input", "huh???"))
print(change_case("snakeCase", "snake"), "snake_case")
