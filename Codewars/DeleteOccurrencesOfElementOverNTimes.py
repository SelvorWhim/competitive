# implemented with list comprehension with side-effects and a global variable
# there's a simpler way to do it with list appends that's probably no less efficient, since Python arrays are dynamic, but I wanted to try this out instead

from collections import Counter

c = Counter()

# for use in list comprehensions with side effects! Naughty...
def count_and_return(x):
    c[x] += 1
    return x

def delete_nth(arr,max_e):
    if max_e <= 0:
        return []
    global c
    c = Counter()
    return [count_and_return(x) for x in arr if c[x] < max_e] # note: condition is evaluated before the function is applied to x, hence < instead of <=
