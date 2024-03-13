"""
sum of integers from 1 to x is x*(x+1)/2, and from x to n is n*(n+1)/2 - (x-1)*x/2
for the pivot, x*(x+1)/2 = n*(n+1)/2 - (x-1)*x/2
-> x*(x+1) = n*(n+1) - (x-1)*x -> x^2 + x = n^2 + n - x^2 + x -> 2*x^2 = n^2 + n
-> x^2 = n*(n+1)/2 -> x = sqrt(n*(n+1)/2)
(since n is positive, x must be positive so only the positive root is relevant.
This is the solution if it's an integer.)
"""

class Solution:
    def pivotInteger(self, n: int) -> int:
        x = sqrt(n*(n+1)/2)
        if not x.is_integer():
            return -1
        return int(x)
