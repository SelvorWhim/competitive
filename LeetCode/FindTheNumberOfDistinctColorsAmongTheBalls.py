from collections import Counter

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}
        color_counts = Counter()
        res = []
        for ball, color in queries:
            if ball in ball_color.keys():
                prev_color = ball_color[ball]
                color_counts[prev_color] -= 1
                if color_counts[prev_color] == 0:
                    del color_counts[prev_color]
            ball_color[ball] = color
            color_counts[color] += 1
            res.append(len(color_counts.keys()))
        return res
