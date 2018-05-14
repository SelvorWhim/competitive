def sum_diagonal_principal(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

def sum_diagonal_secondary(matrix):
    return sum(matrix[i][-i-1] for i in range(len(matrix)))

def diagonal(matrix):
    s1 = sum_diagonal_principal(matrix)
    s2 = sum_diagonal_secondary(matrix)
    return "Principal Diagonal win!" if s1 > s2 else "Secondary Diagonal win!" if s1 < s2 else "Draw!"
