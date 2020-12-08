# idea: keep a dict counting the number of songs for each duration mod 60, then multiply matching pairs
# for mod = 0 the complement is 0, so multiply it n*(n-1) instead. Similar for 30.

from collections import Counter

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod60_durations = Counter(duration % 60 for duration in time)
        pairs = 0
        for duration, count in mod60_durations.items():
            if duration in [0, 30]: # 0 and 30 pair with themselves, so they count differently
                continue
            pairs += count * mod60_durations[60 - duration]
        # add the special cases
        pairs += mod60_durations[0] * (mod60_durations[0] - 1)
        pairs += mod60_durations[30] * (mod60_durations[30] - 1)
        return pairs // 2 # all the above double counted (each pair from both perspectives)
