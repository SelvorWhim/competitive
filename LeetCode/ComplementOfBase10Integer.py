class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bin_digits = bin(N)[2:]
        return int((''.join('1' if d == '0' else '0' for d in bin_digits)), base=2)
