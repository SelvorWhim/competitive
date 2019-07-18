def divide_while_you_can(num, divisor):
    while num % divisor == 0:
        num /= divisor
    return num

class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        num = divide_while_you_can(num, 2)
        num = divide_while_you_can(num, 3)
        num = divide_while_you_can(num, 5)
        return num == 1
