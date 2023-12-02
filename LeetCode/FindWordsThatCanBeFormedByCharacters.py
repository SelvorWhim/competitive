from collections import Counter

def is_good_string(word: str, chars_counter: Counter[str]) -> bool:
    word_counter = Counter(word)
    for letter in word_counter.keys():
        if word_counter[letter] > chars_counter[letter]:
            return False
    return True

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = Counter(chars)
        good_string_length_total = 0
        for word in words:
            if is_good_string(word, chars_counter):
                good_string_length_total += len(word)
        return good_string_length_total
