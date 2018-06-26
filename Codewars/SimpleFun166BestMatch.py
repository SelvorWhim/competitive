def best_match(goals1, goals2):
    return min(range(len(goals1)), key = lambda i:(goals1[i] - goals2[i], -goals2[i])) # tuples make secondary sort - first by difference then by first team's goals (sign flip for ascending)
