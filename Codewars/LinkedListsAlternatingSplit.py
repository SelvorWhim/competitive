# this solution preserves original list structure, but new nodes shallow copy old data, so if the data is a reference type, changing it in one list will affect one of the others

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    # shallow copy of the data, no copy of next
    def clone(self):
        return Node(self.data)
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head == None or head.next == None: # fewer than 2 Nodes in the list
        #return Context(head, None) # that made sense to me but examples say raise an error
        raise ValueError()
    ret = Context(head.clone(), head.next.clone())
    main_it = head.next.next
    ret_its = [ret.first, ret.second]
    i = 2 # or 0, or work with booleans, all I need here is parity. But this way, solution is easily generalized to alternating split between 3 or more lists
    while main_it != None:
        ret_its[i % 2].next = main_it.clone()
        ret_its[i % 2] = ret_its[i % 2].next
        main_it = main_it.next
        i += 1
    return ret
