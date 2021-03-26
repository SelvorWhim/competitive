from collections import Counter

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        A_counters = [Counter(word) for word in A]
        B_counters = [Counter(word) for word in B]
        ret = []
        for i in range(len(A_counters)):
            word_counter_A = A_counters[i]
            valid_subset = True
            for word_counter_B in B_counters:
                if any(word_counter_B[letter] > word_counter_A[letter] for letter in word_counter_B):
                    valid_subset = False
                    break
            if valid_subset:
                ret.append(A[i])
        return ret
