from fractions import Fraction

def mixed_fraction(s):
    num,den = (int(n) for n in s.split("/"))
    sign = "-" if ((num != 0) and ((num < 0) ^ (den < 0))) else ""
    num,den = abs(num),abs(den)
    whole = num//den
    fract = Fraction(num,den) - whole # automatically simplifies
    if fract.numerator == 0:
        return sign + str(whole)
    fract_s = "{}/{}".format(fract.numerator, fract.denominator)
    if whole == 0:
        return sign + fract_s
    return "{}{} {}".format(sign, whole, fract_s)
