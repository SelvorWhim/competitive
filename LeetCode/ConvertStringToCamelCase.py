def to_camel_case(text):
    if len(text) < 2:
        return text
    capped_camel = "".join([word.title() for word in text.replace('-','_').split('_')])
    return capped_camel if text[0].isupper() else capped_camel[0].lower()+capped_camel[1:]
