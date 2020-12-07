# result: success! (with the unshortened form of weight, but I checked equivalence)
# idea: verify length and that the weighted sum of digits is 0 (mod 10)

#Problem        : Verifying Validity
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

def weight(i):
    # if i%2==0:
        # return 1
    # else:
        # return 3
    return 1 if i%2==0 else 3

data = sys.stdin.read().splitlines()
for line in data[1:]:
    if len(line) != 13:
        print("NOT VALID")
    else:
        sum0 = 0
        for i in range(len(line)):
            sum0 += weight(i)*int(line[i])
        if sum0%10 == 0:
            print("VALID")
        else:
            print("NOT VALID")
