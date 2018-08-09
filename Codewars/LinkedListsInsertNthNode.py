class Node(object):
    def __init__(self, data, next = None): # added option to construct with provided next pointer for simplicity
        self.data = data
        self.next = next
    
def insert_nth(head, index, data):
    if index == 0: # separate case because head changes
        return Node(data, head)
    it = head
    while index > 1:
        index -= 1
        it = it.next
    it.next = Node(data, it.next)
    return head
