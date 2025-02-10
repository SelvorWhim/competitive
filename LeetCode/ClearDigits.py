class Solution:
    def clearDigits(self, s: str) -> str:
        chars_to_keep = []
        num_chars_to_delete = 0
        for c in s[::-1]:
            if c.isdigit():
                num_chars_to_delete += 1
            elif num_chars_to_delete > 0:
                num_chars_to_delete -= 1
            else:
                chars_to_keep.append(c)
        return "".join(chars_to_keep[::-1])
