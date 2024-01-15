from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = Counter()
        for [winner, loser] in matches:
            loss_count[loser] += 1
            if winner not in loss_count:
                # keep track of participating players, even if they never lost
                loss_count[winner] = 0
        never_lost = [player for (player, loss_count) in loss_count.items() if loss_count == 0]
        lost_once = [player for (player, loss_count) in loss_count.items() if loss_count == 1]
        return [sorted(never_lost), sorted(lost_once)]
