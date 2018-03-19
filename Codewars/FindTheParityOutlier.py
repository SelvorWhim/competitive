def find_outlier(integers):
    found = [None, None] # even and odd
    foundDuplicate = False
    for n in integers:
        if found[n%2] == None: # first of its parity - we don't yet know which is odd
            if foundDuplicate: # if this parity has none and we've found a duplicate, the other must be the duplicate, so this one is the outlier
                return n
            found[n%2] = n
        elif found[(n+1)%2] != None: # second of its parity, and we have an example of the other
            return found[(n+1)%2] # so the other must be the outlier under assumptions
        else: # duplicate for its parity, and we haven't found an example of the other
            foundDuplicate = True # mark it so that as soon as we find one we can return it
    raise ValueError("input assumptions not met") # under assumptions, the code should not reach this
