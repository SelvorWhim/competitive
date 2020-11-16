import operator as op

ops = {
    0: op.add,
    1: op.sub,
    2: op.mul,
    3: op.truediv
}

def letter_to_num(c):
    return ord(c) - ord('a') + 1

def letter_to_op(c):
    return ops[(letter_to_num(c)-1) % 4]

def testit(s):
    if len(s) % 2 == 0:
        return None
    numbers = [letter_to_num(c) for c in s[0::2]]
    operators = [letter_to_op(c) for c in s[1::2]]
    ret = numbers[0]
    for i in range(len(operators)):
        ret = operators[i](ret, numbers[i+1])
    return ret
