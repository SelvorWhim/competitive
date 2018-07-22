import sys

N = 0
cups = []
for line in sys.stdin.read().splitlines():
    if len(line.split()) == 1: # first line in a case has only a number
        N = int(line)
        cups = [0]*N
        continue
    
    # sort out color and radius:
    c,r = line.split()
    if r.isdigit():
        r = int(r)
    else: # reverse order, and radius is doubled
        c,r = r,int(c)/2
    cups[-N] = {"c":c,"r":r}
    
    N -= 1
    if N <= 0: # case ended
        for cup in sorted(cups, key = lambda cup:cup["r"]):
            print(cup["c"])
