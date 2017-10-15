### INSTRUCTIONS ###
'''
Today, as you were browsing for flights to visit the San Francisco office, you discovered that all flights were on sale for $10. Being a curious developer, you discovered that the bug giving the $10 tickets allows you to pick any number of airports for layovers as long as you don't repeat any stops, and so long as your itinerary starts in JFK and ends in SFO. Using this information, your plan is to see how many unique tickets can be purchased with this bug.


> Input Specifications

In the first line you will be given 0 < N <= 25, the number of airport pairs that have a flight in between them.

The N lines following will be the airport codes (3 letters, A-Z) separated by a space that you can fly between.


> Output Specifications

Print out the integer number of unique ticket paths that can be purchased to travel from JFK to SFO.

'''


### MY SOLUTION (accepted) ###

#Problem        : 2016 Qualifiers - Travel to the West
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys
import copy

flights={}
# destination: 'SFO'
def count_flights(port1,passed):
    if port1 == 'SFO':
        return 1
    passed_new = copy.deepcopy(passed)
    passed_new.append(port1)
    if port1 in flights:
        return sum([count_flights(port2,passed_new) for port2 in flights[port1]]) # sum([]) = 0, and passed_new should prevent infinite loops
    else: # some airports may only have paths to them from data
        return 0

data = sys.stdin.read().splitlines()
N=data[0]
for line in data[1:]:
    port1,port2 = line.split(' ')
    if port1 in flights:
        if port2 not in flights[port1]:
            flights[port1].append(port2)
    else:
        flights[port1] = [port2]

print(str(count_flights('JFK',[])))