# idea: since it's substrings and not subsequences, split into max strings with same consecutive characters, and sum the counts for each
# for each the count is the number of substrings - pick 2 indexes, like the number of handshakes - n*(n+1)/2

class Solution:
    def countHomogenousSingle(self, n: int) -> int:
        return (n * (n + 1)) // 2

    def countHomogenous(self, s: str) -> int:
        prev_char = ''
        total_count = 0
        n = 0
        for c in s:
            if c == prev_char:
                n += 1
            else:
                total_count += self.countHomogenousSingle(n)
                n = 1
                prev_char = c
        total_count += self.countHomogenousSingle(n)
        return total_count % 1000000007
