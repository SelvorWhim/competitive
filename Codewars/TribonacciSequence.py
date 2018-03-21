def tribonacci(signature, n):
    if n <= len(signature):
        return signature[:n]
    for i in range(n-len(signature)):
        signature.append(sum(signature[i:i+3]))
    return signature
