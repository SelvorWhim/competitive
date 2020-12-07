#Problem        : Zipline Hills
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

h = {} # key: hill index, value: hill's height. Just there to help calculate e
e = {} # key: hill index, value: list of hills to which you can travel by zipline from it


def dfs_len(i_from):
    if i_from not in e or not e[i_from]: # no neighbors
        return 0 # path length 0
    return max([(1+dfs_len(i_to)) for i_to in e[i_from]])

data = sys.stdin.read().splitlines()
n=int(data[0])

for i in range(1,len(data)):
    h[i-1] = int(data[i])
for i in range(1,len(h)): # neighbors 1 over
    if h[i] > h[i-1]: # second is higher
        if i in e:
            e[i].append(i-1)
        else:
            e[i] = [i-1]
    else: # first is higher
        if i-1 in e:
            e[i-1].append(i)
        else:
            e[i-1] = [i]
for i in range(2,len(h)): # neighbors 2 over
    if h[i] > h[i-2]: # second is higher
        if i in e:
            e[i].append(i-2)
        else:
            e[i] = [i-2]
    else: # first is higher
        if i-2 in e:
            e[i-2].append(i)
        else:
            e[i-2] = [i]
max_len = max([dfs_len(i_from) for i_from in range(0,len(h))])
print(max_len)
