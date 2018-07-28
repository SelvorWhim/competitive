import numpy as np

def point_vs_vector(point, vector):
    # notation: vector goes from point a to point b
    # adding [0] to project them into 3D space for cross product
    a = np.array(vector[0]+[0])
    b = np.array(vector[1]+[0])
    p = np.array(list(point)+[0])
    ab = b - a # the vector represented as a point
    ap = p - a # vector from the 1st vector's tail to point, represented as a point
    d = np.cross(ab,ap)[2] # sign of the 3rd dimension of cross product indicates side
    return 0 if d==0 else -d/abs(d)
