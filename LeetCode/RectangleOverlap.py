# idea: axis-aligned rectangles overlap if the ranges created by their x values overlap (2 options) and the ranges created by their y values overlap (2 options) - no need to check all 4 combinations of corner overlaps (plus some edge overlaps and inclusions in case of one rectangle is bigger than the other...anyway this is simpler)

def ranges_intersect(a1,a2,b1,b2):
    return a1 < b2 and b1 < a2 # to include touching edges/corners only as intersections change both comparisons to <=

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return ranges_intersect(rec1[0],rec1[2],rec2[0],rec2[2]) and ranges_intersect(rec1[1],rec1[3],rec2[1],rec2[3])
