def dashatize(num):
    if type(num) != int:
        return str(num)
    ret_chars = [] # chars or double chars, meant to be joined
    for d in str(num).strip('-'):
        if int(d) % 2 == 0:
            ret_chars.append(d)
        else:
            ret_chars.append('-' + d + '-')
    return ''.join(ret_chars).replace('--', '-').strip('-')
