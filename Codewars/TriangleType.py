def triangle_type(a, b, c):
    """ return triangle type:
        0 : if triangle cannot be made with given sides
        1 : acute triangle
        2 : right triangle
        3 : obtuse triangle
    """
    a,b,c = sorted([a,b,c]) # reduce redundancy in conditions
    if a + b <= c:
        return 0
    a2,b2,c2 = (x*x for x in (a,b,c))
    if a2 + b2 == c2:
        return 2
    if a2 + b2 < c2:
        return 3
    return 1
