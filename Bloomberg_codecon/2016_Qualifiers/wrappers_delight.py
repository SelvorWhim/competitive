### INSTRUCTIONS ###
'''
You are designing a text editor. Today's task is to implement word wrapping. For our purposes, we will only be wrapping on word boundaries (no hyphenation). Given an input string, with embedded newlines, and a maximum number of characters per line, you need to add newlines in appropriate places to prevent individual lines from getting too long and overflowing the edge of the editor.

Note that the number of characters on a line is inclusive of space characters. For example, if the maximum characters on a line is 10, the line currently contains a seven-letter word, and the next word is 3 letters long, then you will wrap that word to the next line because the separating space character would have pushed the line to 11 characters. Be sure to preserve the newlines that were embedded in the input to start with, regardless of how short that makes a given line.


> Input Specifications

The first line will contain a single integer, n, which is the maximum number of allowed characters on a given line.

The second and final line will be the text to wrap. Note that in order to make the text one line, the input will contain '~' characters representing the embedded newlines. You will replace these with '\n' characters in the output.

There will be no more than one space between words of the input. Consider any punctuation that is not offset by spaces to be part of the bordering word(s).

The input string will be no longer than a paragraph in length.


> Output Specifications

Output the wrapped text, with lines separates by the '\n' newline character. Note that even though embedded newlines were represented as '~' in the input, they should be represented as '\n' in the output.

Also, note that there should be no trailing or leading space characters. If you wrap a line between two words, the space character that separated those words is dropped and replaced by the added newline.

All other characters must be maintained exactly as they were in the input. If an individual word is longer than the maximum line length, leave that word on a line by itself, do not attempt to wrap it.

No extra trailing newlines are expected, unless present in the input.

'''


### MY SOLUTION (accepted) ###

#Problem        : 2016 Qualifiers - Wrapper's Delight
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()
n = int(data[0])
lines = data[1].split('~')
for line in lines:
    words = line.split(' ') # spaces only added back when there's no word wrap
    
    firstinline = True
    for word in words:
        if firstinline: # assuming no word is longer than n. This one's separate because no spaces before it
            printline = word
            charcount = len(word)
            firstinline = False
        
        elif charcount + len(word) + 1 <= n: # +1 for space if word is to be added
            printline += ' ' + word
            charcount += len(word) + 1
        else: # that's a wrap!
            print(printline)
            printline = word
            charcount = len(word)
            firstinline = False # if there's another line, it'll have to reset everything
    print(printline) # if we're out of the loop, we're out of words, so whatever's in the last line still needs printing
    firstinline = True
    # end of a line according to embedded linebreaks. They should be printed as \n because of how the print function works
