# naive O(n^2) time (O(1) space) solution that was just fast enough to be accepted
# pretty sure O(n) is possible with O(n) space usage, maybe even without

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas) # assumed also the length of cost
        for i in range(n):
            curr_gas = 0
            for j in range(n):
                curr_gas += gas[(j+i)%n] - cost[(j+i)%n]
                if curr_gas < 0:
                    break
            if curr_gas >= 0:
                return i
        return -1
