class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j_count = 0
        J_set = set([j for j in J])
        for s in S:
            if s in J_set:
                j_count += 1
        return j_count
