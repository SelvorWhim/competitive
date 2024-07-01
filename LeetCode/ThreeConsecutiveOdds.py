class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive_odds = 0
        for n in arr:
            if n % 2 == 1:
                consecutive_odds += 1
                if consecutive_odds >= 3:
                    return True
            else:
                consecutive_odds = 0
        return False
