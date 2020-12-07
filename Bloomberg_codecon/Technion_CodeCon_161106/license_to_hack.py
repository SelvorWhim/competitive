#Problem        : License to Hack
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()
s=data[0]
n=int(data[1])

chunks = [s[i:i + n] for i in range(0, len(s), n)] # works even if not divisible by n

outstr = ''
for i in range(0,len(chunks)): # whole blocks of length n
    if i%2==0:
        outstr += chunks[i][::-1] # reverse even indexed chunks, including the first
    else:
        outstr += chunks[i] # leave the rest as is
print(outstr)