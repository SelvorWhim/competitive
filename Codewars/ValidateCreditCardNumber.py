def validate(num):
    digits = [int(d) for d in str(num)]
    n = len(digits)
    for i in range(n % 2, n, 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return sum(digits) % 10 == 0
