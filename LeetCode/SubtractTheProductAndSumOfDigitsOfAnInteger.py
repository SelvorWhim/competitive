from operator import mul

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        product = reduce(mul, digits, 1)
        return product - sum(digits) # not absolute value, based on test case
