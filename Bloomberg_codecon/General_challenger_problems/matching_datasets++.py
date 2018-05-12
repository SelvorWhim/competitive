### INSTRUCTIONS ###
'''
You've worked on a report for weeks and its all ready to submit, when all of a sudden your data is gone! Fortunately, you still have a hard copy of your charts, and you're able to estimate the approximate value of each datapoint.

When you regenerate your data, you know that the exact values of the data points will be close to what you eyeballed, but you don't know what order they'll be in. By finding the closest data elements, you'll be able to be confident in your report and the data as well.

NOTE:The test cases for this problem are considerably larger than the Matching Datasets problem.


> Input Specifications

Your program will take
    The number of elements K that are in each dataset.(0<=K<=1000)
    This will be followed by K lines representing the original dataset (which is comprised of points from the chart). Each line will be a comma separated list of values.
    The final K lines after that will be the new dataset. Each line will be a comma separated list of values here as well.


> Output Specifications

Based on the input, print out K lines where each line consists of two values where
    The first value denotes the element (0,1,2...K-1) in the original dataset.
    The second value, comma separated, will be the index of the closest point in the new dataset.
Note that the output should be sorted in ascending order of element indices in the original dataset.

'''


### MY SOLUTION (accepted - both for Matching Datasets and for Matching Datasets++) ###

#Problem        : Matching Datasets
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys
from math import sqrt


# assuming euclidean distance
# assuming each point is a list of 4 numerical coordinates
def dist(p1,p2):
    return sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2+(p2[2]-p1[2])**2)


set_orig = [] # list of lists 4 values each
set_new = [] # same

data = sys.stdin.read().splitlines()
K = int(data[0])
for line in data[1:K+1]:
   set_orig.append([float(c) for c in line.split(',')])
for line in data[K+1:]:
    set_new.append([float(c) for c in line.split(',')])

# but what if 1 in the new matches 2 in the old as the nearest neighbor?
for i in range(len(set_orig)): # if K=0..?
    p1 = set_orig[i]
    argmin = 0
    mindist = dist(p1,set_new[0])
    for j in range(1,len(set_new)): # if K=1..?
        p2 = set_new[j]
        newdist = dist(p1,p2)
        if newdist < mindist:
            mindist = newdist
            argmin = j
    print("%d,%d"%(i,argmin))
