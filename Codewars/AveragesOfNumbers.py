def averages(arr):
    return [(x1+x2)/2 for x1,x2 in zip(arr[:-1],arr[1:])] if arr else []
