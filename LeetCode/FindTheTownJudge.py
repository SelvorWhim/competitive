class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cant_be_judge = set()  # people who trust other people
        num_trusters = [0]*n
        for truster, trustee in trust:
            cant_be_judge.add(truster)
            num_trusters[trustee - 1] += 1
        for i in range(n):
            if num_trusters[i] == n-1 and (i+1) not in cant_be_judge:
                return i + 1
        return -1
