"""
Simple Fun #352: Reagent Formula
https://www.codewars.com/kata/59c8b38423dacc7d95000008
"""

def isValid(formula):
    contains = [x in formula for x in range(9)] # 0-8 for indexing convenience
    if contains[1] and contains[2]:
        return False
    if contains[3] and contains[4]:
        return False
    if not contains[7] and not contains[8]:
        return False
    return contains[5] == contains[6]
