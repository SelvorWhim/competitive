from math import ceil

def char_avg(s,i1,i2):
    if i2 >= len(s):
        return s[i1]
    return chr((ord(s[i1]) + ord(s[i2]))//2) # "average" char, rounded down

def testit(s):
    return "".join(char_avg(s,i,i+1) for i in range(0,len(s),2))
