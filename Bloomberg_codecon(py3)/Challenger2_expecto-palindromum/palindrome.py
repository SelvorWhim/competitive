#Problem        : Expecto Palindronum
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()
S = data[0] # length assumed nonzero and bounded by 100

## brute force method 1 (abandoned):
# even = False
# for pal_len in range(len(S),(2*len(S))):
    # even = not even # I can't even
    # flag
    # if even:
        # for j in range(i/2): # trying to confirm polynomial of this length. If failed, need longer
            # refpt = i/2 - 1 # index of reflection point for assumed palindrome length
            # j_reflect = refpt + (refpt - j)
            # if S[j] != S[j_reflect]:
                # break

## brute force method 2 (awkward attempt at the next, abandoned):
# pal_len = len(S)
# for i in range(len(S),(2*len(S))):
    # pal_len = i
    # even = not even # I can't even
    # sub_len = 2*len(S) - pal_len
    # sub_start = 
    # sub = S[]

## brute force method 3
pal_len = len(S)
for i in range(len(S)): # i is the length of the added tail
    pal_len = len(S) + i
    sub = S[0:-i]
    if i == 0:
        sub = S # because S[0:0] gives wrong result - otherwise cuts i off the end
    if sub == sub[::-1]: # pythonic way to reverse a string
        break

print(pal_len)