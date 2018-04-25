def digit_sum(num_str):
    return sum(int(c) for c in num_str)

def order_weight(weights):
    weights = weights.split()
    return " ".join(sorted(weights, key=lambda w: (digit_sum(w), w))) # primary sort by "weight", secondary alphabetical
