from itertools import groupby

def grouped_counter(word):
    return [(l,len(list(group))) for l,group in groupby(word)] # list of tuples, each with character and its count, grouped by consecutive appearances

class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        match_count = 0
        stretched_counts = grouped_counter(S)
        for word in words:
            query_counts = grouped_counter(word)
            if len(stretched_counts) != len(query_counts):
                continue
            match_flag = True
            for (lq,cq),(ls,cs) in zip(query_counts,stretched_counts):
                if lq!=ls or cq > cs or (cq==1 and cs==2):
                    match_flag = False
                    break
            if match_flag:
                match_count += 1
        return match_count
