''' INSTRUCTIONS '''

# For this problem, you are required to do the following:
	# Given a number X (X will be a number in a base between base-2 and base-16), find the minimum base that can be associated with X.
	# *Example: The minimum base associated 385 is base-9 (as it needs to have a base that supports the digit 8 which is its highest value digit). Similarly, the minimum base associated with B95 is base-12.
	# Convert X from this base to a value X_10 in base-10.
	# Do the same for another number Y and call its value in base-10 as Y_10
	# Print out the sum of these two numbers in base-10, ie X_10 + Y_10

# > INPUT Specifications

# Your program will take
	# A number X in base-m (X >= 0, 2 = m = 16)
	# A number Y in base-n (Y >= 0, 2 = n = 16)

# You can assume that X and Y when converted to base-10 will fit in a long long (C++).

# > OUTPUT Specifications

# Based on the input, print out the sum of X_10 and Y_10




''' MY SOLUTION ''' # accepted

#Problem        : Base Arithmetic
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

hexmap = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

def min_base(num):
    chars = list(num)
    max_digit = 1 # minimum base is 2
    for char in chars:
        #if char.isdigit():
            #max_digit = max(max_digit,int(char)) # or hexmap
        #else:
            #max_digit = max(max_digit,hexmap[char.upper()])
        max_digit = max(max_digit,hexmap[char]) # assuming all letter symbols are uppercase
    return max_digit+1

def to_base_10(num,base):
    if base == 10:
        return int(num)
    symbols = list(num)
    numsum = 0
    for i in range(len(symbols)):
        numsum += hexmap[symbols[0-(i+1)]] * (base**i)
    return numsum

data = sys.stdin.read().splitlines() # need to input file or stop input after 2 lines (w ctrl+Z?)
X = data[0]
Y = data[1]

X_base = min_base(X)
Y_base = min_base(Y)
X_10 = to_base_10(X,X_base)
Y_10 = to_base_10(Y,Y_base)
print(X_10+Y_10)
