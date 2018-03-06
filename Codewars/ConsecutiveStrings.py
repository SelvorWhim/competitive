''' idea: we want a subarray of length k with the largest sum of string lengths
 to avoid summing all k every time (in case of large k),
 add the last and remove the first every time
 (keeping track of the maximum length and the index from which it occurred).
 To get the first longest, update the maximum only when strictly increasing.
 Only "sum" the strings at the very end, when we know which ones give the max.
 That way we get O(n + len(res)) time and O(n) extra space regardless of other string lengths.
'''
def longest_consec(strarr, k):
    if len(strarr) < k or k <= 0:
        return ""
    curr_lensum = sum([len(str) for str in strarr[:k]]) # lensum for first k
    max_lensum = curr_lensum # length of longest consecutive string sum found so far
    max_i = 0 # first index of longest consecutive string sum found so far
    for i in range(len(strarr) - k):
        curr_lensum += len(strarr[i+k]) - len(strarr[i]) # running lensum updated using only changed members
        if curr_lensum > max_lensum:
            max_lensum = curr_lensum
            max_i = i+1
    return "".join(strarr[max_i : max_i+k]) # getting actual string after components are found
