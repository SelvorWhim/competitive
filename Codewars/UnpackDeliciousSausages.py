sausages = "I()@l|║1¦"

def unpack_sausages(truck):
    print(truck)
    ret = []
    undamaged = 0
    for package in truck:
        for box in package:
            if len(box) == 6 and box[0] == "[" and box[-1] == "]":
                box_types = set(box[1:-1])
                if len(box_types) == 1 and box[1] in sausages: # if all the same, just check one
                    undamaged += 1
                    if undamaged % 5 != 0: # one in 5 is my payment :P
                        ret += box[1:-1]
    return " ".join(ret)
