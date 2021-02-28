ops = {"+": lambda x, y: x + y, "*": lambda x, y: x * y, "-": lambda x, y: x - y, "/": lambda x, y: x / y, }


def zero(*args):  # your code here
    if args == ():
        return 0
    else:
        op, value = args[0].split()
        return ops[op](0, int(value))


def one(*args):  # your code here
    if args == ():
        return 1
    else:
        op, value = args[0].split()
        return ops[op](1, int(value))


def two(*args):  # your code here
    if args == ():
        return 2
    else:
        op, value = args[0].split()
        return ops[op](2, int(value))


def three(*args):  # your code here
    if args == ():
        return 3
    else:
        op, value = args[0].split()
        return ops[op](3, int(value))


def four(*args):  # your code here
    if args == ():
        return 4
    else:
        op, value = args[0].split()
        return ops[op](4, int(value))


def five(*args):  # your code here
    if args == ():
        return 5
    else:
        op, value = args[0].split()
        return ops[op](5, int(value))


def six(*args):  # your code here
    if args == ():
        return 6
    else:
        op, value = args[0].split()
        return ops[op](6, int(value))


def seven(*args):  # your code here
    if args == ():
        return 7
    else:
        op, value = args[0].split()
        return ops[op](7, int(value))


def eight(*args):  # your code here
    if args == ():
        return 8
    else:
        op, value = args[0].split()
        return ops[op](8, int(value))


def nine(*args):  # your code here
    if args == ():
        return 9
    else:
        op, value = args[0].split()
        return ops[op](9, int(value))


def plus(arg):  # your code here
    return f"+ {arg}"


def minus(arg):  # your code here
    return f"- {arg}"


def times(arg):  # your code here
    return f"* {arg}"


def divided_by(arg):  # your code here
    return f"/ {arg}"
