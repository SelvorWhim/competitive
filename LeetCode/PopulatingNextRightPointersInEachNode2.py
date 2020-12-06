"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.last_in_level = {} # maps level number, starting from 0, to last, or None if we haven't seen one yet
        self.connect_recursive(root, 0)
        return root

    def connect_recursive(self, node, level: int):
        if node == None:
            return
        if level in self.last_in_level:
            self.last_in_level[level].next = node
        self.last_in_level[level] = node
        self.connect_recursive(node.left, level + 1)
        self.connect_recursive(node.right, level + 1)
