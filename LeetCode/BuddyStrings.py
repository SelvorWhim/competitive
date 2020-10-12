class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        mismatches = [-1, -1]
        for i in range(len(A)):
            if A[i] != B[i]:
                if mismatches[0] < 0:
                    # first mismatch
                    mismatches[0] = i
                elif mismatches[1] < 0:
                    # 1 previous mismatch
                    mismatches[1] = i
                else:
                    # 2 previous mismatches - can't have 3
                    return False
        if mismatches[0] < 0:
            # no mismatches found, so they're buddy strings iff there are at least 2 identical letters
            return len(set(A)) < len(A)
        elif mismatches[1] < 0:
            # 1 mistmatch found, no switch possible to fix it
            return False
        else:
            # exactly 2 mismatches - they're buddy strings iff it's a swap
            return A[mismatches[0]] == B[mismatches[1]] and A[mismatches[1]] == B[mismatches[0]]
