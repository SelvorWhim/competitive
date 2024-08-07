digit_to_word = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
}

tens_digit_to_word = {
    #1: "Ten", # covered by teens
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety",
}

teens_to_word = {
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
}

# could go higher
powers_of_1000_to_word = {
    0: "",
    1: " Thousand",
    2: " Million",
    3: " Billion",  # short scale ;)
}

def numberToWordsUnderThousand(num: int):
    assert(0 < num < 1000)
    words = []
    hundreds = num // 100
    tens = (num % 100) // 10
    ones = num % 10
    if hundreds >= 1:
        words += [digit_to_word[hundreds], "Hundred"]
    if tens >= 2:
        words.append(tens_digit_to_word[tens])
    if tens == 1:
        teens = num % 100
        words.append(teens_to_word[teens])
    elif ones >= 1:
        words.append(digit_to_word[ones])
    return " ".join(words)


class Solution:
    def numberToWords(self, num: int) -> str:
        phrases = []
        if num == 0:
            return "Zero"
        power_of_1000 = 0
        while num > 0:
            if num % 1000 > 0:
                phrases.append(numberToWordsUnderThousand(num % 1000) + powers_of_1000_to_word[power_of_1000])
            power_of_1000 += 1
            num = num // 1000
        return " ".join(phrases[::-1])
