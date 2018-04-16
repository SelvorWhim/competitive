from math import sqrt

class Vector:
    def __init__(self, coords):
        self.coords = coords
    
    def equals(self, v):
        return self.coords == v.coords
    
    def __str__(self):
        return str(tuple(self.coords)).replace(" ","")
    
    # must be Vector of same dimension
    def add(self, v):
        if len(v.coords) != len(self.coords):
            raise ValueError("Vector dimensions must match")
        return Vector([c1+c2 for c1,c2 in zip(self.coords, v.coords)])
    
    def subtract(self, v):
        if len(v.coords) != len(self.coords):
            raise ValueError("Vector dimensions must match")
        return Vector([c1-c2 for c1,c2 in zip(self.coords, v.coords)])
    
    def dot(self, v):
        if len(v.coords) != len(self.coords):
            raise ValueError("Vector dimensions must match")
        return sum([c1*c2 for c1,c2 in zip(self.coords, v.coords)])
    
    def norm(self):
        return sqrt(sum([c*c for c in self.coords]))
