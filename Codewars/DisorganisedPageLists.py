def find_page_number(pages):
    wrong = []
    last = 0
    for page in pages:
        if page != last + 1:
            wrong.append(page)
        else:
            last = page
    return wrong
