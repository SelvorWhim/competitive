### INSTRUCTIONS ###
'''
As part of a team project to build an instant messaging program, you have to work around your teammate's buggy compliance filter.

The compliance filter works based on an algorithm which determines if certain messages can pass through the system and if they should be flagged. Usually the compliance filter system has a dictionary of black listed words which it filters out.

However, due to your teammate's programming error the compliance filter system appears to only allow words that are palindromes or anagrams of palindromes (i.e. can make a palindrome when re-arranged).

For example:
    abba
    aabb (this one is an anagram of abba or baab)
    civic
    deified
    mom
    mmo
    radar
While a fix is being worked on, you are tasked with writing an add on that will determine if a word can pass through the this system.


> Input Specifications

Your program will take
    A string S denoting the word to be tested. All letters in the alphanumeric input will be lowercase (1 <= LENGTH(S) <= 500), and there may be numbers and symbols.


> Output Specifications

Based on the input,
    Print out yes if the input would pass through the system
    Print out no if the input would fail the system

'''


### MY SOLUTION (accepted) ###

#Problem        : A Compliance Problem
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys
from itertools import groupby

# Basic idea: anagrams of palindromes have even numbers of each letter with the possible exception of one

def is_palinagram(s):
    letters = []
    for letter in S :
       letters.append(letter)
       letters.sort() # if only it were that simple in real life # default sort for strings is alphabetic
    grouped_letters = [(key,len(list(group))) for key, group in groupby(letters)]
    
    odd_found = False
    for (letter,count) in grouped_letters:
        if count%2 == 1:
            if odd_found: # second odd
                return False
            else: # first odd
                odd_found = True
    return True



data = sys.stdin.read().splitlines()
S = data[0]
if is_palinagram(S):
    print('yes')
else:
    print('no')

#original filename palinagram
