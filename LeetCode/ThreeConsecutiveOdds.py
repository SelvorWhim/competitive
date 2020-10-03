class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecurive_odds = 0
        for n in arr:
            if n % 2 == 1:
                consecurive_odds += 1
                if consecurive_odds == 3:
                    return True
            else:
                consecurive_odds = 0
        return False
