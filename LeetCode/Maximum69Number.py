class Solution:
    def maximum69Number (self, num: int) -> int:
        numstr = str(num)
        i = numstr.find('6')
        if i < 0:
            return num
        return int(numstr[:i] + '9' + numstr[i+1:])
