def revrot_chunk(chunk):
    if sum(int(d)**3 for d in chunk) % 2 == 0:
        return chunk[::-1]
    else:
        return chunk[1:]+chunk[0]

def revrot(s, sz):
    if sz <= 0 or not s or sz > len(s):
        return ""
    return "".join([revrot_chunk(s[i*sz:(i+1)*sz]) for i in range(len(s)//sz)])
