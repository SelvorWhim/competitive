def mark_spot(n):
    if (type(n) != int) or (n < 0) or (n%2 == 0):
        return "?" # what arrr you trying to pull here?
    half_rows = ["{}X{}X\n".format(i*" ", (2*n-3-2*i)*" ") for i in range(0,n-2,2)] # except the middle one with the single X
    return "".join(half_rows + [(n-1)*" " + "X\n"] + half_rows[::-1]) # would've used "\n".join but a trailing newline is expected
