# I was surprised this is even guaranteed to work...
# once the number is composed of digits smaller than 5, adding it to its reverse must produce a palindrome
# I guess eventually the digits will be small enough so it'll work.
# or maybe it tends to "smooth" out all differences a bit at a time even if it doesn't happen all at once.

def reverse_num(n):
    return int(str(n)[::-1])

def palindrome_chain_length(n):
    steps = 0
    # this will break by return assuming the iteration works without the number getting too big, I don't know a closed formula
    while True:
        rn = reverse_num(n)
        if n == rn:
            return steps
        n += rn
        steps += 1
