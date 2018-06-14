def alternate_sort(l):
    neg = sorted([x for x in l if x < 0], reverse = True)
    pos = sorted([x for x in l if x >= 0])
    combo = [None]*(len(l))
    alter_len = min(len(neg),len(pos))
    combo[:2*alter_len:2] = neg[:alter_len]
    combo[1:2*alter_len+1:2] = pos[:alter_len]
    combo[2*alter_len:] = neg[alter_len:] if len(neg) > len(pos) else pos[alter_len:]
    return combo
