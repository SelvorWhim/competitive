def maxSequence(arr):
    max_sum = 0
    curr_sum = 0
    for n in arr:
        if curr_sum + n > 0:
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        else:
            curr_sum = 0
    return max_sum
