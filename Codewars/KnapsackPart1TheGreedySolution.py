def knapsack(capacity, items):
    sorted_items = sorted(enumerate(items), key = lambda item: item[1][1]/item[1][0], reverse = True) # enumerate to preserve indexes, sort by value/size ratio
    take = [0]*len(items) # output, once incremented
    i = 0 # index in sorted list
    while capacity > 0 and i < len(items):
        i_original,item = sorted_items[i] # item with the next best ratio
        can_carry = capacity // item[0] # as many of that item as you can carry (might be 0) - note integer division
        take[i_original] += can_carry
        capacity -= item[0] * can_carry # reduce capacity by the weight of that
        i += 1
    return take
