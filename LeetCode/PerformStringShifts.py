# end result is like making a single shift (or rotation) that's the sum of the rest
class Solution:
    def rotateStringLeft(s: str, rotateBy: int) -> str:
        return s[rotateBy:] + s[:rotateBy]
    
    def sumShifts(shifts: List[List[int]]) -> int:
        return sum(amount if dir == 0 else -amount for dir, amount in shifts)
    
    def stringShift(self, s: str, shifts: List[List[int]]) -> str:
        # figure out the index to rotate by
        rotateBy = Solution.sumShifts(shifts) % len(s)
        # rotate the given strign by that amount
        return Solution.rotateStringLeft(s, rotateBy)
