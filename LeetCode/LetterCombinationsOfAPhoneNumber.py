import itertools

phone_digit_to_letters = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        letter_lists = itertools.product(*[phone_digit_to_letters[digit] for digit in digits])
        return [''.join(letter_list) for letter_list in letter_lists]
