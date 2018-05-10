def score_throws(radiuses):
    score = 0
    for r in radiuses:
        if r < 5:
            score += 10
        elif r <= 10:
            score += 5
    if score > 0 and score == 10*len(radiuses): # empty list shouldn't get bonus, based on example
        score += 100 # bonus
    return score
