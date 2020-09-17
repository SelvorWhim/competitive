"""
the question is whether the robot's movement is bounded when the instructions are repeated infinitely
at the end of the instructions, the robot will be some distance from the origin
facing one of 4 directions relative to its original heading
if the distance is 0, it's bounded regardless of direction
if the distance is >0 and the direction is its original, repeating will cause it to continue in one direction forever
if the distance is >0 but the direction is opposite to the original, then repeating the instructions twice
will cause it to return to the origin, and overall the movement will be bounded
if the distance is >0 but the direction is perpendicular to the original, then repeating the instructions
4 times will cause it to return to the origin (like walking the sides of a square), and movement is bounded
so the answer is false only if final distance is 0 and direction is same as original.
"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0,1), (1,0), (0,-1), (-1,0)] # go right in circular array to rotate right, left to rotate left
        loc = [0,0]
        dir_i = 0
        for step in instructions:
            if step == 'R':
                dir_i += 1
            elif step == 'L':
                dir_i -= 1
            elif step == 'G':
                direction = directions[dir_i % 4]
                loc[0] += direction[0]
                loc[1] += direction[1]
        print(loc, dir_i)
        return (loc == [0,0]) or (dir_i % 4 != 0)
