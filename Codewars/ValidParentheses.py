def valid_parentheses(string):
    open_count = 0
    for c in string:
        if c == '(':
            open_count += 1
        elif c == ')':
            open_count -= 1
            if open_count < 0:
                return False
        # any other characters are ignored (treated as valid)
    return (open_count == 0)
