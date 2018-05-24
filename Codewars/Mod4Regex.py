import re

'''
idea: an integer is divisible by 4 in each of 3 cases:
1. it's a single digit divisible by 4
2. it ends in an odd digit followed by an even digit that's not divisible by 4
3. it ends in an even digit followed by an even digit that is divisible by 4
the rest deals with the formatting as described.
tests should have used search instead of match, as it is I've added .* to allow anything to surround the brackets
'''

class Mod:
    mod4 = re.compile(r".*\[[+-]?([048]|(\d*([13579][26]|[02468][048])))\].*") #Your regular expression here
