### INSTRUCTIONS ###
'''
War has been declared in Westeros. All houses, great and small, are vying for the iron throne.

In this problem, you will be given a list containing: the name of each house, the number of sworn knights the house has, and the names of any houses sworn as bannermen. Bannermen are houses who swear their allegiance to a greater house, which we refer to as their liege lord. Beginning with the lowest houses (those without any bannermen), you will evaluate whether or not a liege lord is overthrown by one of his bannermen.

A liege lord is overthrown if the number of sworn knights that the lord has is at least 3 less than the number one of his bannermen has. The overthrowing bannerman will then take the place of his liege lord in the house hierarchy while the former lord is relegated to bannerman. If multiple bannermen fit this description, the one with the most sworn knights wins, with ties broken in ascii order of house name. Proceeding in this way, you will continue on up the chain of houses until you reach the iron throne.


> Input Specifications

The first line will contain a single integer, n, the number of houses in the game.

This will be followed by n lines, one per house.

Each line contains a space-separated list. The first token is the name of the house. The second token is the number of sworn knights the house has. The third token is an integer, b, the number of bannermen the house has. The final 'b' tokens are the names of that house's bannermen (subordinate houses).

Note that house names are made up of an unbroken string of letters (possibly mixed case) with no punctuation or spaces contained.

There will be no more than 50 houses provided.


> Output Specifications

Ouput the levels of the resulting Westeros house hierarchy, in level order, one level per line. The house in control of the iron throne is printed first, all of its bannermen will be on the second line, and so on.

Note that because we proceed bottom to top, it is possible for a house to move up multiple levels in the chain, but no house may descend more than one level.

Sort each level in strict ascii order (case-sensitive), irrespective of the number of sworn knights.

'''


### MY SOLUTION (accepted) ###

#Problem        : 2016 Qualifiers - A Game of Thrones
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys
import copy

houses = []
banners = {} # child nodes
lord = {} # parent pointers
levels = {} # hierarchy levels. Key = level, 0-indexed, value - group of houses at that level.
knights = {} # assuming knights don't switch houses when a lord is overthrown
# note: overthrown lord becomes bannerman, doesn't say what happens to overthrower's bannermen
# assumption: overthrower and overthrown switch levels, otherwise nothing changes. Final tree doesn't matter, only levels.

## read data
data = sys.stdin.read().splitlines()
n = int(data[0]) # n<=50
for line in data[1:]:
    deets = line.split(' ')
    house,n_knights,b = deets[0:3]
    houses.append(house)
    knights[house] = int(n_knights)
    banners[house] = deets[3:]
    for banner in deets[3:]:
        lord[banner] = house # assuming one lord per banner - a tree structure
houses2 = copy.deepcopy(houses)

## find hierarchy
for house in houses2:
    if house not in lord: # house has no lord - it's at the top, assumed the only
        levels[0] = [house]
        break
level = 0
while houses2:
    next_level = []
    for house in levels[level]:
        for banner in banners[house]:
            next_level.append(banner)
        houses2.remove(house)
    if next_level:
        levels[level+1] = next_level
        level += 1
max_level = level
# level should now be the biggest level index in the hierarchy

for level in range(max_level,0,-1): # the overthrowing level. All except the top bottom-up.
    overthrown = set([]) # set because there may be several bannermen that can overthrow their lord
    for house in levels[level]: # find all houses one level above that can be overthrown by this level
        if knights[house] >= 3 + knights[lord[house]]:
            overthrown.add(lord[house])
    for house in overthrown:
        takers = sorted(banners[house], key=lambda h: (0-knights[h], h)) # primary sort reverse by number of sworn knight, secondary by ascii of house
        levels[level-1].remove(house) # deposed!
        levels[level].append(house)
        levels[level-1].append(takers[0])
        levels[level].remove(takers[0])
        if house in lord: # else, they have the iron throne!
            lord[takers[0]] = lord[house] # otherwise will try to overthrow again on the next level and can't move up
            banners[lord[house]].append(takers[0])
            banners[lord[house]].remove(house)
    # moving bottom up, should be possible for a house to rise multiple levels

for level in levels: # the final tally
    level_str = ''
    for house in sorted(levels[level]): # not sure this is strict ASCII order but it worked
        level_str += house + ' '
    level_str.rstrip()
    print(level_str)
    
# original filename - treefight