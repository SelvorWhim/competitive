# note they didn't specify what order the output should be in

from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        output = []
        c = Counter(nums)
        most_common_num = c.most_common()[0][0]
        while c[most_common_num] > 0:
            curr_row = []
            for x, _ in c.most_common():
                curr_row.append(x)
                c[x] -= 1
                if c[x] == 0:
                    del c[x]
            output.append(curr_row)
        return output
