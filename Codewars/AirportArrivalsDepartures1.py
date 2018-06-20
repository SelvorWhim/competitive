def flap_display(lines, rotors):
    ress = []
    for line,line_rotors in zip(lines,rotors):
        run_sum = 0
        res = ""
        for c,rotor in zip(line,line_rotors):
            run_sum += rotor
            res += ALPHABET[(ALPHABET.index(c) + run_sum) % len(ALPHABET)] # TODO: optimize string concatenations and add reverse mapping to prevent having to index every time
        ress.append(res)
    return ress
