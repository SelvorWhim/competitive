def solution(s):
    ret = [s[i:i+2] for i in range(0,len(s),2)]
    if len(s)%2 == 1:
        ret[-1] = ret[-1]+'_'
    return ret
