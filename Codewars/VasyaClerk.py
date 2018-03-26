def tickets(people):
    bills = {25:0,50:0,100:0}
    for bill in people:
        if bill == 25:
            bills[25] += 1
        elif bill == 50: # must give a 25 in change
            if bills[25] >= 1:
                bills[25] -= 1
                bills[50] += 1
            else:
                return "NO"
        elif bill == 100:
            if bills[50] >= 1 and bills[25] >= 1: # 50s are given only here, no reason to use an extra 2 25's when we have a 50
                bills[25] -= 1
                bills[50] -= 1
                bills[100] += 1
            elif bills[25] >= 3: # but if there's no 50s, we can give change in 25s if possible
                bills[25] -= 3
                bills[100] += 1
            else:
                return "NO"
        else:
            raise ValueError()
    return "YES"
