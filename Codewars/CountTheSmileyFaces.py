valid_eyes = [':',';']
valid_noses = ['-','~']
valid_mouths = [')','D']

def is_smiley(s):
    return (2 <= len(s) <= 3) and (s[0] in valid_eyes) and (s[-1] in valid_mouths) and (len(s) == 2 or s[1] in valid_noses)

def count_smileys(arr):
    return sum(1 for s in arr if is_smiley(s))
