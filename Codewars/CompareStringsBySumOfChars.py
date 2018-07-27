def s_sum(s):
    return sum(ord(c) for c in s.upper()) if s and s.isalpha() else 0

def compare(s1,s2):
    return s_sum(s1) == s_sum(s2)
