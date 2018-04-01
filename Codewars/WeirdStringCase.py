def word_to_weird_case(word):
    return "".join([word[i].upper() if i%2==0 else word[i].lower() for i in range(len(word))])

def to_weird_case(string):
    return " ".join([word_to_weird_case(word) for word in string.split()])
