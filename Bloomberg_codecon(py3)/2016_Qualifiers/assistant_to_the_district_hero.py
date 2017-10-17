### INSTRUCTIONS ###
'''
You've just been hired to help your district hero, Lieutenant Positivity, to fight crime. Your job is to figure out what is the highest number of crimes the Lieutenant can stop with his positivity. 

Normally, a hero would stop all crimes in his district, but Lieutenant Positivity, like all heroes, has a flaw. The Lieutenant can not travel in the negative direction, meaning the Lieutenant can only move from A,B to C,D if A <= C and B <= D

Luckily for you, figuring out the highest number of crimes the Lieutenant can stop should be straightforward since your district is a small grided city(50x50) with your HQ being at 0,0. You also live in a pretty safe district, so there are never more than 20 crimes being committed at a given time.


> Input Specifications

First, you will be given the number of crime coordinates on its own line. Each line to follow will be the integer coordinates of a crime in the form of X Y.


> Output Specifications

You should output the integer number of the highest number of crimes that Lieutenant Positivity can reach

'''


### MY SOLUTION (accepted) ###

#Problem        : 2016 Qualifiers - Assistant to the District Hero
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

# actually, no need to save path...
def dfs(adj_mat,curr_node,path_len):
    adjs = adj_mat[curr_node]
    neighbors = [j for j in range(n) if adjs[j]==1] # all nodes to which there is a link from curr
    if neighbors == []:
        return path_len
    else:
        return max([dfs(adj_mat,j,path_len+1) for j in neighbors])

data = sys.stdin.read().splitlines()
n = int(data[0])
points=[]
for line in data[1:]:
    pt = line.split()
    points.append([int(pt[0]),int(pt[1])]) # whitespace split. Tuple/list of 2 added to list of points.

mat = [[0 for x in range(n)] for y in range(n)] # Adjacency matrix
for i in range(n):
    for j in range(n):
        if i==j:
            continue # don't add self-loops, don't want to get stuck in one
        if points[i][0] <= points[j][0] and points[i][1] <= points[j][1]: # point j is bigger along both coordinates
            mat[i][j] = 1 # adjacency added. NOT symmetrical!

# from here the graph can be navigated using adjacency matrix alone.
# we're looking for the longest path - the one that visits the most nodes.
lengths = []
for start in range(n):
    lengths.append(dfs(mat,start,1))
print(max(lengths))

#original filename positive_path