import re

def abbreviate_word(w):
    w = w.group(0) # since I'm working with regex
    if len(w) < 4:
        return w
    return "{}{}{}".format(w[0],len(w)-2,w[-1])

def abbreviate(s):
    return re.sub(r"[a-zA-Z]+",abbreviate_word,s) # for multiple delimiters which must be kept, this is simpler than my attempts without regex
