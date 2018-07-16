def loop_size(node):
    p1 = node # jumps by 1
    p2 = node.next # jumps by 2
    while p1 != p2: # with these jumps, if there's a loop, eventually they'll meet, somewhere in the loop
        p1 = p1.next
        p2 = p2.next.next
    p1 = p1.next # move it from being equal
    loop_len = 1
    while p1 != p2: # now go round the loop one more time, measuring it
        p1 = p1.next
        loop_len += 1
    return loop_len
