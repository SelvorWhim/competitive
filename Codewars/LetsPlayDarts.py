'''
# idea: convert to polar coordinates, check radius for special areas,
# then check angle for pie slice
# I didn't find a clear specification of the slice shape at the link
# so I'll assume symmetry - equal angles (20th of a circle each)
# and the 20,6,3,11 are centered on top, right etc.
# note: the ring measurements are given in diameters, not radii
'''

from math import sqrt, atan2, pi, floor

slice_score = [6,13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10]
slice_angle = pi/10 # in radians - 2pi/20

def polar_coords(x,y):
    r = sqrt(x*x + y*y)
    a = atan2(y, x)
    print(r,a)
    return (r,a)

# x,y,r units are mm, a (angle) units are radians
def get_score(x,y):
    r,a = polar_coords(x,y)
    if r > 170:
        return "X"
    if r < 6.35:
        return "DB"
    if r < 15.9:
        return "SB"
    modifier = ""
    if 162 < r < 170: # double ring. Outer bound was already ruled out but for clarity...
        modifier = "D"
    elif 99 < r < 107: # triple ring
        modifier = "T"
    slice_index = floor(((a + slice_angle/2) // slice_angle) % 20)
    return modifier + str(slice_score[slice_index])
