#Problem        : Anagram Count
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

# note: for single word with no anagram, 0. For any group of anagrams, the size of the group. Sum over groups
# groupby? nah

import sys
import collections
from itertools import groupby

data = sys.stdin.read().splitlines()
n=int(data[0])

words = [] # each as a counter, like a bag of letters, which can be compared
for line in data[1:]:
   words.append(collections.Counter(line.lower()))

total = 0
for word in words:
    count = 0
    for word2 in words:
        if word==word2:
            count += 1
            del word2 # what about itself?
    if count > 1:
        total += 1 # because each anagram is counted separately...not what I intended, but works?

print(str(total))