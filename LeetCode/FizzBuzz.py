def fizzBuzzUnit(i):
    if i%15==0:
        return "FizzBuzz"
    if i%3==0:
        return "Fizz"
    if i%5==0:
        return "Buzz"
    return str(i)

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in range(n):
            l.append(fizzBuzzUnit(i+1))
        return l
