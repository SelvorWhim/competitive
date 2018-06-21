'''
# idea: convert to polar coordinates, check radius for special areas,
# then check angle for pie slice
# I didn't find a clear specification of the slice shape at the link
# I assumed symmetry - equal angles (20th of a circle each)
# and the 20,6,3,11 are centered on top, right etc.
# (and it worked for the test cases)
'''

from math import sqrt, atan2, pi, floor

# note: the measurements in instructions are given in diameters, these are radii
R_DB = 6.35
R_SB = 15.9
R_T_IN = 99
R_T_OUT = 107
R_D_IN = 162
R_D_OUT = 170
R_BOARD = 170
slice_angle = pi/10 # in radians - 2pi/20
slice_score = [6,13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10] # starting with rightmost going counter-clockwise

def polar_coords(x,y):
    r = sqrt(x*x + y*y)
    a = atan2(y, x)
    return (r,a)

# x,y,r units are mm, a (angle) units are radians
def get_score(x,y):
    r,a = polar_coords(x,y)
    if r > R_BOARD:
        return "X"
    if r < R_DB:
        return "DB"
    if r < R_SB:
        return "SB"
    modifier = ""
    if R_D_IN < r < R_D_OUT: # double ring. Outer bound was already ruled out but for clarity...
        modifier = "D"
    elif R_T_IN < r < R_T_OUT: # triple ring
        modifier = "T"
    slice_index = floor(((a + slice_angle/2) // slice_angle) % 20) # added half slice because 0 degrees is mid-slice, not between 
    return modifier + str(slice_score[slice_index])
