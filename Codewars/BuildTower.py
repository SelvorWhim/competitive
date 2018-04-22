def tower_builder(n_floors):
    return [((n_floors - i)*' ' + (2*i - 1)*'*' + (n_floors - i)*' ') for i in range(1,n_floors+1)]
