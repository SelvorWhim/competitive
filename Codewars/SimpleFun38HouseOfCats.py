def house_of_cats(legs):
    if legs % 2 != 0: # the tests don't cover this case but it makes sense, if the number of legs isn't even the situation is impossible according to the description
        return []
    return list(range((legs%4)//2, (legs//2)+1, 2))
