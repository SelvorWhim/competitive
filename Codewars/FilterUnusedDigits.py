def unused_digits(*args):
    remain = set("0123456789")
    for n in args:
        remain -= set(str(n))
    return "".join(sorted(remain))
