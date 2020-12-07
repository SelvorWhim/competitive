#Problem        : Chemistry 101
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()
n=int(data[0])

prereq = {}
for line in data[1:n+1]:
    l = line.split(' ')
    prereq[l[0]] = l[2:]

order = data[n+1].split(' ')

def check_order():
    for i in range(0,len(order)):
        chem = order[i]
        if chem in prereq:
            for p in prereq[chem]:
                if p not in order[:i]:
                    return 'BOOM!'
    return 'SAFE!'

print(check_order())