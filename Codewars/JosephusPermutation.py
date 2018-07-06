def josephus(items,k):
    n = len(items) # original length
    j = 0
    res = []
    for i in range(n):
        j = (j+k-1)%len(items) # new length, which is shorter by 1 - counting with looping # -1 to compensate for previous deletion, and works with first item when j is initialized at 0
        res.append(items[j])
        del items[j]
    return res
