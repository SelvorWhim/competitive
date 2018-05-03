def move_zeros(arr):
    arr2 = [x for x in arr if (isinstance(x, bool) or x != 0)] # without isinstance, False == 0
    return arr2 + (len(arr)-len(arr2))*[0]
