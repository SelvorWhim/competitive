### INSTRUCTIONS ###
'''
One of the golf courses down at Chelsea Piers in NYC is trialing a new system of automated cars. A car's computer breaks the course down in sections and can move from one section to another. This particular golf course was split into sections in this way:
    1	2	3
    4	5	6
    7	8	9
        0	 
However due to a small bug in the software, a car can only move in L shapes (e.g. 1 step horizontally, 2 steps vertically) for example, from 1 to 8, or from 1 to 6, or from 4 to 0.

Given this course, can you find out how many unique paths are there for a car to get from 1 to 9 in exactly N moves ? A move is one trip of a car from one section to another (e.g. a move is going from 1 to 6, regardless of the exact sections passed on the way).

Unique Path - A path which is different from others in at least one move.

Example of a path from 1 to 9 in 10 moves is - 1 6 1 6 1 6 1 6 7 2 9.

Another example - 1 6 1 6 1 6 7 2 7 2 9.


> Input Specifications

Your program will take
    A number N that denotes the number of moves the car has to make to reach from 1 to 9 (1<=N<=10)


> Output Specifications

Based on the input,
    Print out the number of possible unique paths P.

'''


### MY SOLUTION (accepted) ###

#Problem        : Finals Spring 2015 - Golf Course
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

# they mean knight moves, not diagonals
# without the 0, there's 2 directions to move, with at least 4 moves and any even number higher than that requiring some back and forth
# uh...N is very bounded, I could hard code this...
# also almost every square has 2 moves leading from it with a few having 3, could brute force it
# 2^N paths <= (2^10-3^10)=(1k,60k), no biggie
# could optimise by saving results from smaller counts, dynamic programming style

import sys

neighbors = {0:[4,6],1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],6:[0,1,7],7:[2,6],8:[1,3],9:[2,4]} # 5 is unreachable
def count_paths(steps,curr):
    if steps == 0:
        if curr == 9:
            return 1
        else:
            return 0
    else: # and there are mountains yet to climb
        return sum([count_paths(steps-1,j) for j in neighbors[curr]])

data = sys.stdin.read().splitlines()
N = int(data[0])

if N<4:
    print(0)
else:
    print(count_paths(N,1))
# original filename: knight_brute