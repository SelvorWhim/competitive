from collections import Counter, OrderedDict

class Solution:
    def sortString(self, s: str) -> str:
        charcount = Counter(s)
        sorted_charcount = OrderedDict(sorted(charcount.items(), key=lambda item: item[0]))
        ret_chars = []
        to_delete = set()
        while(sorted_charcount):
            for c in sorted_charcount.keys(): # in order, since it's an OrderedDict initialized with sorted dict
                if sorted_charcount[c] == 0: # can't del inside iterator
                    to_delete.add(c)
                else:
                    ret_chars.append(c)
                    sorted_charcount[c] -= 1
            for c in reversed(sorted_charcount.keys()): # in reverse order; uses iterators, shouldn't copy dict
                if sorted_charcount[c] == 0: # can't del inside iterator
                    to_delete.add(c)
                else:
                    ret_chars.append(c)
                    sorted_charcount[c] -= 1
            for c in to_delete:
                del sorted_charcount[c]
            to_delete = set()
        return ''.join(ret_chars)
