def number(n, f=None):
    return f(n) if f else n

def zero(f=None):
    return number(0, f)
def one(f=None):
    return number(1, f)
def two(f=None):
    return number(2, f)
def three(f=None):
    return number(3, f)
def four(f=None):
    return number(4, f)
def five(f=None):
    return number(5, f)
def six(f=None):
    return number(6, f)
def seven(f=None):
    return number(7, f)
def eight(f=None):
    return number(8, f)
def nine(f=None):
    return number(9, f)

def plus(arg2):
    return lambda x: x + arg2
def minus(arg2):
    return lambda x: x - arg2
def times(arg2):
    return lambda x: x * arg2
def divided_by(arg2):
    return lambda x: x // arg2 # based on examples, integer division