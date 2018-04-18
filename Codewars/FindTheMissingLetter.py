def find_missing_letter(chars):
    prev = chars[0]
    for c in chars[1:]:
        if ord(c) != ord(prev) + 1:
            return chr(ord(prev)+1)
        prev = c
