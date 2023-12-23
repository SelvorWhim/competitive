# dealing with 2D integer coordinates here,
# but let's represent them with the built-in complex type for funsies

DIRECTION_TO_COMPLEX = {
    'N': complex(0,1),
    'S': complex(0, -1),
    'E': complex(1,0),
    'W': complex(-1, 0),
}

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = complex(0,0)
        visited = set([curr])
        for step in path:
            curr += DIRECTION_TO_COMPLEX[step]
            if curr in visited:
                return True
            visited.add(curr)
        return False
