# idea: for ranges give rough bounds, then we check for edge cases before adding to answer

def digit_char_array_to_int(digits):
    return int(''.join(digits))

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_s = str(low)
        high_s = str(high)
        min_len = len(low_s)
        max_len = len(high_s)
        ret = []
        for num_len in range(min_len, max_len+1):
            min_start_digit = 1 if num_len > min_len else int(low_s[0])
            max_start_digit = 10-num_len if num_len < max_len else min(int(high_s[0]), 10-num_len)
            for start_digit in range(min_start_digit, max_start_digit+1):
                new_num = digit_char_array_to_int([str(start_digit + d) for d in range(num_len)])
                if low <= new_num <= high:
                    ret.append(new_num)
        return ret
