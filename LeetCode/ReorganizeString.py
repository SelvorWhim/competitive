# hah, I do this in my head when organizing pairs of socks; from this vast experience,
# it's possible whenever the most frequent letter appears at most 1 more time than the rest of the letters combined
# arrange the most frequent, then the next between them, and if it doesn't reach the end, keep arranging between the first, but once it does, just layer every type. Easiest after getting a counter of letter occurrences in the string

from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        stacks = [] # list of lists, to be flattened later
        i = 0
        for char, count in Counter(S).most_common(): # todo: optimize: only need to set apart the most common type
            if len(stacks) == 0:
                stacks = [[char] for i in range(count)]
            else:
                for j in range(i, i+count):
                    stacks[j % len(stacks)].append(char)
                i += count
        if i < len(stacks) - 1:
            return ''
        stacks = [''.join(stack) for stack in stacks] # convert char sublists into strings
        return ''.join(stacks)
