def speedify(s):
    out_chars = (len(s)+25) * [' '] # as big as we might need - strip any unused spaces later
    for i in range(len(s)):
        out_chars[i+(ord(s[i])-ord('A'))] = s[i]
    return ''.join(out_chars).rstrip()
