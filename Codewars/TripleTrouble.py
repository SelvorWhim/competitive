def triple_double(num1, num2):
    triples = set() # digits that appear in triples in num1
    doubles = set()
    curr = ''
    curr_len = 0
    for d in str(num1):
        if d == curr:
            curr_len += 1
        else:
            curr = d
            curr_len = 1
        if curr_len >= 3:
            triples.add(d)
    curr = ''
    for d in str(num2):
        if d == curr: # already a double
            if d in triples:
                return True
        else:
            curr = d
    return False
