import math

class Matrix:
    def __init__(self, rows: list):
        self._rows = [Vector(row) for row in rows]

    def __str__(self):
        rowbuffer = ""
        for row in self._rows:
            rowbuffer = rowbuffer + "\n" + str(row) # yes, off by one \n, I know
        return rowbuffer
    
    def __repr__(self):
        return [row._vect for row in self._rows]
    
    # no, I am NOT doing matmul things.
    

class Vector:
    def __init__(self, vect:list):
        self._vect = vect
    
    def __str__(self):
        return str(self._vect)

    def __repr__(self):
        return self._vect
    
    def __neg__(self):
        result = []
        for item in range(len(self._vect)):
            result.append(-self._vect[item])
        return Vector(result)
        
    def __add__(self, vect2: object):
        result = []
        assert len(self._vect) == len(vect2._vect)
        for item in range(len(self._vect)):
            result.append(self._vect[item] + vect2._vect[item])
        return Vector(result)
    
    def __sub__(self, vect2: object): # identical to add, but subtracts in for loop instead
        return self._vect + vect2
    
    def __mul__(self, scalar: float): # scalar, not dot product, similar to prev 2 in structure
        result = []
        for item in range(len(self._vect)):
            result.append(self._vect[item] * scalar)
        return Vector(result)
    
    def __rmul__(self, scalar: float):
        return self * scalar
    
    def magnitude(self):
        squaresum = 0
        for item in self._vect:
            squaresum = item**2 + squaresum
        return math.sqrt(squaresum)
        

vec1 = Vector([4,5,6,7])
vec2 = Vector([1,2,3,4])
print(2*vec1)
print(vec1*3)
vec3 = vec1 + vec2
print(vec3.magnitude())
mat1 = Matrix([[1,2,4,5], [2,2,2,1], [1,2,3,4], [4,2,4,2]])
print(mat1)