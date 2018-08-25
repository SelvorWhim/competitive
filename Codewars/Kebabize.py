def capital_to_kebab(c):
    return "-" + c.lower() if c.isupper() else c if c.isalpha() else ""

def kebabize(s):
    return "".join(capital_to_kebab(c) for c in s).lstrip("-")
