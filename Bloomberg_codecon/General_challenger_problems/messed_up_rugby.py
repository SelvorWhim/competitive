### INSTRUCTIONS ###
'''
A team of developers from New York visits London and decides to try their hands at Rugby. None of them quite remember the exact rules so they just use the rules of American Football where you can score 2, 3 or 7 points at a time.

When they talk to you afterwards, they tell you that the final score of the game was 38 - 0. After facepalming, you are curious to find all possible ways to score 38 points.

Write a program that, given a score X, prints all possible combinations of the messed up conversions (7 points), tries (3 points), and kicks (2 points) that would make up this score.


> Input Specifications

Your program will take a target score between 0 and 222.


> Output Specifications

Based on the input, print out one row for each combination of messed up conversions, tries, and kicks that would get to that score, each column delimited by a space. The output should be in ascending order of touchdowns, field goals, and then safeties. If the score is not achievable, just output 0 0 0

'''


### MY SOLUTION (accepted) ###

#Problem        : Messed up Rugby
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

def printriplet(a,b,c):
    print(str(a)+' '+str(b)+' '+str(c))

data = sys.stdin.read().splitlines()
X = int(data[0])

pts_conversion = 7
pts_try = 3
pts_kick = 2

# related to the coin problem...
# input is bounded and loop length will keep decreasing and I think the number of ways is roughly proportional to the number if iterations anyway, so let's brute force it
ways = 0 # just to check edge case
for i in range(X//pts_conversion + 1):
    subtotal = i*pts_conversion
    if subtotal == X:
        printriplet(i,0,0)
        ways += 1
        break
    for j in range((X-subtotal)//pts_try + 1):
        subtotal = i*pts_conversion + j*pts_try
        if subtotal == X:
            printriplet(i,j,0)
            ways += 1
            break
        for k in range((X-subtotal)//pts_kick + 1):
            subtotal = i*pts_conversion + j*pts_try + k*pts_kick
            if subtotal == X:
                printriplet(i,j,k)
                ways += 1
                break
if ways == 0: # impossible sum
    print('0 0 0')