'''
idea: this is like an expression made of 2 kinds of parentheses ()[],
where you have to remove all the substrings composed of balanced parentheses
this solution is like using a stack, but mutates the original data instead of using extra space
'''

opposite = {"NORTH":"SOUTH", "SOUTH":"NORTH", "EAST":"WEST", "WEST":"EAST"}

def dirReduc(arr):
    i = 1
    while i < len(arr): # len not constant in this case! hence while
        if opposite[arr[i]] == arr[i-1]:
            del arr[i]
            del arr[i-1]
            i = max(i-1,0)
        else:
            i += 1
    return arr
