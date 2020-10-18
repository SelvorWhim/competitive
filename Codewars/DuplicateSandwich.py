def duplicate_sandwich(arr):
    seen = set()
    for word in arr:
        if word in seen:
            double = word
            break
        seen.add(word)
    i1 = -1
    i2 = -1
    for i,word in enumerate(arr):
        if word == double:
            if i1 < 0:
                i1 = i
            else:
                i2 = i
                break
    return arr[i1+1:i2]
