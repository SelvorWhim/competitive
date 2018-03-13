def find_it(seq):
    unpaired = set()
    for n in seq:
        if n in unpaired:
            unpaired.remove(n)
        else:
            unpaired.add(n)
    return unpaired.pop() # based on givens, there should be exactly one element remaining
