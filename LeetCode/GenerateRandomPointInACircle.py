"""
uniform in polar coordinates would be easy, in euclidean it's harder
how about generate a random point in the bounding square and check if it's in the circle, else try again?
>75% chance every time
(there are better ways, but this is simple)
"""

import random

def point_in_circle(dx, dy, r):
    return dx*dx + dy*dy <= r*r # no need to sqrt

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        in_circle = False
        while not in_circle:
            x = random.uniform(self.x - self.r, self.x + self.r)
            y = random.uniform(self.y - self.r, self.y + self.r)
            in_circle = point_in_circle(self.x - x, self.y - y, self.r)
        return [x,y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
