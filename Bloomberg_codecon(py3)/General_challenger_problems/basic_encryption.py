### INSTRUCTIONS ###
'''
With all the talk about cryptography and encryption, your friend has come up with the following basic encryption method:
    An initial array of data (called A) is an array of integers. Each integer can have a value between 0 and 255, inclusive.
    The encrypted array of data (called E) is the same size as A. Each entry of the encrypted array E is the sum of all entries in A that are not in the same position as the entry being calculated. For example, with the original array A consisting of:
        1 2 3 4 5
    The encrypted array E will be:
        14 13 12 11 10
The first entry of E is the sum of the second through fifth entries in A (2+3+4+5=14).
You feel this method of encryption is faulty. To demonstrate this, write a program to take an array encrypted by your friend's method and decrypt it!


> Input Specifications

Your program must read from STDIN
    A single integer N (1 <= N <= 5000) indicating the number of entries in the array.
    N lines each containing a single integer between 0 and 100000000, inclusive, formatted with no unnecessary leading zeros.


> Output Specifications

If the decrypted array is valid (i.e. all entries are integers between 0 and 255), print each element of the decrypted array with no unnecessary leading zeros in order, one element per line.

If there is no possible decrypted array, output the string NO SOLUTION on a single line.

If there are multiple valid decrypted arrays, output the string MULTIPLE SOLUTIONS on a single line.

'''


### MY SOLUTION (accepted) ###

#Problem        : Basic Encryption
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()
N = int(data[0])
arr = [int(line) for line in data[1:]]

flag = True
if N == 1:
    print ("MULTIPLE SOLUTIONS")
    flag = False
else:
    sumarry = int(sum(arr)/(N-1))
    decrypted = [(sumarry-X) for X in arr]

if flag:
    if sum(decrypted) != sumarry: # not sure if this case is possible
        print("NO SOLUTION")
        flag = False
    for d in decrypted:
        if d%1 != 0 or d < 0 or d > 255:
            print("NO SOLUTION")
            flag = False
            break

if flag:
    for d in decrypted:
        print(d)