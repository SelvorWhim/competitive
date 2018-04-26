def is_valid_octet(n_str):
    return n_str.isdigit() and (n_str[0] != '0' or n_str == '0') and int(n_str) <= 255 # isdigit also returns false for empty strings and negatives

def is_valid_IP(str):
    nums = str.split('.')
    return (len(nums) == 4) and all(is_valid_octet(n) for n in nums)
