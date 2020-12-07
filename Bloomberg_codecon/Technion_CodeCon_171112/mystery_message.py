# result: success!
# idea: key adds to letter value (mod 26), we have the message decrypted and encrypted plus stuff irrelevant to the task which is easy to separate.

#Problem        : Mystery Message
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()

for line in data :
    treats = line.split() # first 7 are encrypted, last is 1st but decrypted
    enc = treats[0]
    dec = treats[5] # weekdays, apparently, so 5 not 7
    X = (ord(enc[0])-ord(dec[0])+26)%26
    print(X)
