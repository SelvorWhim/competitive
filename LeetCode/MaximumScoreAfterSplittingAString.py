# idea: calculate score for first possible split, then go char by char and keep the running score, remembering the max

class Solution:
    def maxScore(self, s: str) -> int:
        max_score = s[1:].count('1') + int(s[0] == '0')  # score for the first possible split
        curr_score = max_score
        print(curr_score)
        for c in s[1:-1]:  # going over all non-empty splits to compare scores
            if c == '0':
                curr_score += 1
                max_score = max(max_score, curr_score)
            else: # assuming '1'
                curr_score -= 1
            print(curr_score)
        return max_score
