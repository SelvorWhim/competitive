"""idea: iterate backwards over shifts and letters and apply the running shift sum to each letter"""

# lowercase English only
def shift_letter(letter, shift):
    shifted_ord = (((ord(letter) - ord('a')) + shift) % 26) + ord('a')
    return chr(shifted_ord)

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        letters = [c for c in s]
        shift_sum = 0
        for i in range(len(shifts)):
            shift_sum += shifts[-1 - i]
            letters[-1 - i] = shift_letter(letters[-1 - i], shift_sum)
        return ''.join(letters)
