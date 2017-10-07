### INSTRUCTIONS ###
'''
A palindrome is a word that reads the same backward and forward. 

Given a string S, you are allowed to convert it to a palindrome by adding 0 or more characters in front of it. 

Find the length of the shortest palindrome that you can create from S by applying the above transformation. 


> Input Specifications

Your program will take
    A string S ( 1 ≤ Length(S) ≤ 100) where each character of S will be a lowercase alphabet (Between 'a' to 'z')


> Output Specifications

For each input, print out an integer L denoting the length of the shortest palindrome you can 
generate from S.

'''


### MY SOLUTION (accepted) ###

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