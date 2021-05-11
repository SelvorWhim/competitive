"""
ranges from taking the first k to taking the last k, so try all the combinations, shifting one numbr at a time
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_score = curr_score = sum(cardPoints[:k])
        for i in range(1, k+1):
            curr_score += cardPoints[-i] - cardPoints[k-i]
            max_score = max(max_score, curr_score)
        return max_score
