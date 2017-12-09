# brute force solution, should be n*log(n) if division and mod by 10 is constant time, for interval of size n

def isSelfDividing(n):
    if n == 0: # TODO: replace with do-while in C++
        return False
    n1 = n
    while n1 > 0:
        d = n1%10
        if d == 0 or n % d != 0:
            return False
        n1 = n1//10
    return True
            

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [i for i in range(left, right + 1) if isSelfDividing(i)]
