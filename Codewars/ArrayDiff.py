def array_diff(a, b):
    forbidden = set(b)
    return [x for x in a if x not in forbidden]
