def find_missing(arr):
    d = arr[1] - arr[0]
    abs_d = abs(d)
    if abs_d > abs(arr[2] - arr[1]): # second term is missing
        return arr[0] + d/2
    last = arr[1]
    for x in arr[2:]:
        if abs(x-last) > abs_d:
            return x-d
        last = x
    raise Exception("YOU LIED TO ME") # description assumptions must be false :P
