### INSTRUCTIONS ###
'''
Your teammate tried to fix the bug, but only managed to make it worse! Now the filter will only accept words that are already palindromes.

You are now tasked with writing another add-on that determines how many different words you can send through the system given a set of characters.

For example:
    bbaa can be sent in two different ways: abba and baab
    bbaacc can be sent in six different ways: baccab, abccba, acbbca, cabbac, bcaacb, and cbaabc.


> Input Specifications

Your program will take
    A string S denoting the set of characters to be tested. All letters in the alphanumeric input will be lowercase (1 <= LENGTH(S) <= 500)


> Output Specifications

Based on the input, print out the total number of unique palindromes that can be created from the input.

'''


### MY SOLUTION (accepted) ###

#Problem        : Yet Another Compliance Problem
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys
from math import factorial
from itertools import groupby

def palicount(S):
    letters = []
    for letter in S :
       letters.append(letter)
       letters.sort() # if only it were that simple in real life (would that it were so simple) # default sort for strings is alphabetic
    grouped_letters = [(key,len(list(group))) for key, group in groupby(letters)]
    
    odd_found = False
    sum_counts = 0
    counts_over_1 = []
    for (letter,count) in grouped_letters:
        if count%2 == 1:
            if odd_found: # second odd
                return 0 # not a palinagram, as seen in previous -> 0 ways
            else: # first odd
                odd_found = True
        sum_counts += count // 2 # //2 - just the letters to be ordered, the second half will reflect it; odd has to be in the middle, so it's not part of the count
        if count//2 > 1: # identical letter ordering should not be included
            counts_over_1.append(count/2) # /2 - just the letters to be ordered, the second half will reflect it
    # ways to order the first half of the palindrome (not including middle if odd)
    orders = factorial(sum_counts) # could be problematic for large enough number. DO I have any non-combinatorial way to count it?
    for n in counts_over_1:
        orders /= factorial(n) # seems to work right, even with like length 300, so what's wrong with it? Maybe they DIDN'T want division?
    return int(orders)

data = sys.stdin.read().splitlines()
S = data[0]

print(palicount(S))