def accum(s):
    return "-".join([s[i].upper() + i*(s[i].lower()) for i in range(len(s))])
