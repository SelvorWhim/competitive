def diamond_row(i, n):
    return (n - i)*' ' + (2*i + 1)*'*' + '\n'

def diamond(n):
    if n < 0 or n % 2 == 0:
        return None
    rows = []
    mid_row = n//2 # index of middle row
    for i in range(mid_row): # up to, not including middle row
        rows.append(diamond_row(i, mid_row))
    for i in range(mid_row, -1, -1): # down from and including middle row
        rows.append(diamond_row(i, mid_row))
    return ''.join(rows)
