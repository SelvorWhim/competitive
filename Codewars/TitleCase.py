def title_case(title, minor_words = ""):
    minor_words = minor_words.lower().split()
    return " ".join([word.lower() if (i>0 and word.lower() in minor_words) else word.title() for i,word in enumerate(title.split())])
