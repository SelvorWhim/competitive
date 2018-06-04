# assuming every chicken contains 1 head and 2 legs and every cow contains 1 head and 4 legs
# we get the equations A+B=x and 2A+4B=y for A chickens and B cows (confusingly, x and y are given while A and B are the unknowns)
# this can be algebraically reduced to B=y/2-x and A=x-B

def animals(heads, legs):
    n_cows = legs//2 - heads
    n_chickens = heads - n_cows
    return (n_chickens, n_cows) if (legs % 2 == 0) and (n_cows >= 0) and (n_chickens >= 0) else "No solutions"
