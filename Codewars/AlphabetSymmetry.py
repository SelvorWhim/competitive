def solve(arr):
    return [len([0 for i in range(len(word)) if i == (ord(word[i].lower())-ord('a'))]) for word in arr]
