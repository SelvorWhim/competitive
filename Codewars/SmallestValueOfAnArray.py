def find_smallest(numbers,to_return):
    i_min = min((i for i in range(len(numbers))),key=lambda i:numbers[i])
    return {'index':i_min, 'value':numbers[i_min]}[to_return]
