# pretty sure this is not the intended solution but hey I know about so many dunder methods now!
class add:
    def __init__(self,x):
        self.x = x
    
    def __call__(self, y):
        return add(self.x + y)
    
    def __eq__(self, other_num):
        return self.x == other_num
    
    def __add__(self, other_num):
        return self.x + other_num
    
    def __sub__(self, other_num):
        return self.x - other_num
