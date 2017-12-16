# O(n) time for n squares on the board, O(1) extra space

def at(grid,x,y,w,h):
    if x < 0 or x >= w or y < 0 or y >= h:
        return 0
    return grid[y][x]

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        if h == 0:
            return 0
        w = len(grid[0])
        perimiter = 0
        for x in range(w):
            for y in range(h):
                if at(grid,x,y,w,h) == 1:
                    perimiter += 4
                    for (dx,dy) in [(1,0),(-1,0),(0,1),(0,-1)]: # for each step to an orthogonal neighbor
                        if at(grid, x+dx, y+dy, w, h) == 1:
                            perimiter -= 1
        return perimiter
