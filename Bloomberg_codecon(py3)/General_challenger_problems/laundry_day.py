### INSTRUCTIONS ###
'''
It's laundry day, and, as usual, you've been putting this off for quite some time. Also, unfortunately, you lacked the foresight to actually ensure all your dirty laundry stayed in your hamper whilst it accumulated (what? we can't ALL be underwear basketball pros!).

Begrudgingly, you've gathered up all the clothing you could find and sent them through the wash. Now you have a disheveled pile of clean, albiet disorganized, accoutrements. You come to the realization that you probably lost some items in the fray, so now it's time to fold and figure out what's gone missing!

To get a good idea of the state of your wardrobe, count up the number of distinct shirts, pants, and underwear you have as you go through the laundry. Also pair up your socks, noting the number of pairs of each kind of sock and if there are any lonely souls (single (and ready to mingle) socks).


> Input Specifications

Each article of clothing will have its own separate line. You have a penchant for hoarding, so there is no guarantee as to the number of pieces, but you can assure yourself that each article can be easily categorized by description (name).

Articles of clothing will be fed in as line-delimited list. See below for examples.


> Output Specifications

Output should be an alphabetically (case-insensitive) sorted, line-delimited list of the articles of clothing along with their count. Each field (count, category) should be separated by a pipe (|). If you come across a sock without a soulmate, the count should be designated by a 0 (zero). Socks that are in pairs should be on separate lines from the socks of the same category without pairs, and should come before the pairless sock. See below for examples.

'''


### MY SOLUTION (accepted) ###

#Problem        : Laundry Day
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys
from collections import Counter

data = sys.stdin.read().splitlines()

#sc = sorted(Counter(data).items()) # I was stuck for a while because I missed the case-insensitive bit, and the shown examples were all lowercase
sc = sorted(Counter(data).items(), key=lambda t: str.lower(t[0])) 

def outLine(name, count):
    print(str(count)+"|"+name)

for key,count in sc:
    if key.endswith("sock"):
        if (count//2) > 0:
            outLine(key, count//2)
        if (count%2) == 1:
            outLine(key, 0)
    else:
        outLine(key, count)
