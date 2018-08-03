def find_even_index(arr):
    n = len(arr)
    s_left = 0
    s_right = sum(arr[1:])
    for i in range(len(arr)):
        if s_left == s_right:
            return i
        s_left += arr[i]
        s_right -= (arr[i+1] if (i+1 < n) else 0)
    return -1
