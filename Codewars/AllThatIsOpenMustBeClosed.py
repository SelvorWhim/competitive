def is_balanced(s, caps):
    closer = {caps[i]:caps[i+1] for i in range(0,len(caps),2)} # create opener-closer mapping dictionary
    open = []
    for c in s:
        if open and closer[open[-1]] == c: # closing last pair opened
            open.pop()
        elif c in closer.keys(): # opening a new pair
            open.append(c)
        elif c in closer.values(): # closing a pair it didn't open, and not a single-value pair like quotes
            return False
    return len(open) == 0 # True if all open pairs have been closed
