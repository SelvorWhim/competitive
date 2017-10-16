### INSTRUCTIONS ###
'''
You are an entry level hero and your first task from the Lannisters of Justice is to break into the throne room of the Mad Mathemagician. The only issue is that his throne is guarded by a numeric password that is solved by following a specific ordering of operations on an expression. 

No one before you was successful, but that was because they didn't figure out that the Mathemagician followed his own Mad order of operations; he ordered it by the amount of strokes it took his iron pen to write the operators. The ordering you have deduced (from first to last) is: subtraction( - ), division( / ), addition( + ), multiplication( * )


> Input Specifications

You will be given a single line of character input of no more than 100 characters that is a valid math expression using integers and math operations. Example could be something as simple as 3+4 or something a little more complex, such as 3*4+12/6. Your input will only contain the 4 operators and numbers, no other characters.


> Output Specifications

You will need to output the solution to the equation when applying the Mathemagician's order of operations. All output will be a single integer value.

'''


### MY SOLUTION (accepted) ###

#Problem        : 2016 Qualifiers - Lannisters of Justice
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from __future__ import print_function
import sys

ops = ['-','/','+','*']
digits = ['0','1','2','3','4','5','6','7','8','9']
def use_op(a,op,b):
    if op == '-':
        return a-b
    elif op == '/':
        return a/b
    elif op == '+':
        return a+b
    else:
        return a*b


data = sys.stdin.read().splitlines()
s = data[0]
elements = []
num = ''
for c in s:
    if c in digits:
        num += c
    else:
        elements.append(int(num))
        num = ''
        elements.append(c) # if current is not number, it's an operator
if num != '':
    elements.append(int(num))
# assuming starts and ends with numbers and no 2 operators in a row and no spaces or such

while ops != []: # originally len(elements) > 1
    i = 0
    while i < len(elements): # because its length changes
        c = elements[i]
        if c == ops[0]: # first order of operations for now
            newnum = use_op(elements[i-1],c,elements[i+1])
            for j in range(3):
                del elements[i-1] # delete the 2 numbers and operator we just calculated
            elements.insert(i-1,newnum) # now put the calculated value where they were
        else: # because the next may be the same op, and the next is now in the same index
            i += 1
    # reaching here, we calculated all expressions including the first operation in the order
    del ops[0] # so next iteration, we'll get a new one

print(str(int(float(elements[0])))) # heh