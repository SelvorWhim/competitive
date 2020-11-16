ops = {
    0: '+',
    1: '-',
    2: '*',
    3: '/'
}

def letter_to_num(c):
    return ord(c) - ord('a') + 1

def letter_to_op(c):
    return ops[(letter_to_num(c)-1) % 4]

def testit(s):
    if len(s) % 2 == 0:
        return None
    expression = ''.join(str(letter_to_num(s[i])) if i%2==0 else letter_to_op(s[i]) for i in range(len(s)))
    # using eval as a quick and dirty way to resolve order of operations...
    return eval(expression)
