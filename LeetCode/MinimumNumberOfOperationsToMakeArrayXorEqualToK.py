# XOR is parity, you just need every digit to match eventually,
# so XOR everything (including k) and see how many 1 bits you're left with

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_all = k
        for num in nums:
            xor_all ^= num
        return xor_all.bit_count()
