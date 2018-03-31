def unique_in_order(iterable):
    return [iterable[i] for i in range(len(iterable)) if i==0 or iterable[i] != iterable[i-1]]
