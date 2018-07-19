# chunk is expected to be a string of digits
def _revrot_chunk(chunk):
    if sum(int(d) for d in chunk) % 2 == 0: # even digit sum; note 3rd power is even iff number itself is even
        return chunk[::-1] # reverse
    else: # odd digit sum
        return chunk[1:] + chunk[0] # rotate

def revrot(s, sz):
    if sz <= 0 or not s or sz > len(s): # no full chunks
        return ""
    return "".join(_revrot_chunk(s[i*sz:(i+1)*sz]) for i in range(len(s)//sz)) # ignores trailing partial chunk
