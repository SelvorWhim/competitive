def expanded_form(num):
    mod_base = 1
    expansion = []
    while (mod_base <= num):
        mod_base *= 10
        rem = num % mod_base
        if rem > 0:
            expansion.append(str(rem))
            num -= rem
    return " + ".join(expansion[::-1])
