# TIME LIMIT EXCEEDED. Depending on how optimized set(permutations) is, this is either (10 choose num) or 10!, which exceeds the limit depending on the constant
# This worked for smallest (or largest) nums where the number of combinations was smaller, but too slow for the middle ones
# improvement ideas: separately find all valid hours for each number if lit bits, and all valid minutes (pre-filtering by the 11 and 59 limits), and pick combinations from complementary pairs

from itertools import permutations as p

# expected input: list of binary digits with first 4 representing hours and last 6 representing minutes
def time_str(time_binary):
    hour_binary_str = ''.join(time_binary[:4])
    hour_decimal = int(hour_binary_str,2)
    minute_binary_str = ''.join(time_binary[4:])
    minute_decimal = int(minute_binary_str,2)
    if hour_decimal <= 11 and minute_decimal <= 59:
        return str(hour_decimal) + ':' + str(minute_decimal).rjust(2,'0') # rjust adds leading 0 on the left if minunte number is single-digit
    # else return None

class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num < 0 or num > 10:
            return []
        base_vector = ['1']*num + ['0']*(10-num) # as chars so I can join later
        time_strs = [time_str(v) for v in set(p(base_vector))] # set of permutations gives all binary vectors (lists of digits) of length 10 (4+6) with <num> 1 digits without repetition, function converts each to string in required format
        return [t for t in time_strs if t != None] # filter out strings with too many hours/monutes
