import math

class Matrix:
    def __init__(self):
        pass

class Vector:
    def __init__(self, vect:list):
        self._vect = vect
    
    def __str__(self):
        return str(self._vect)

    def __repr__(self):
        return self._vect
        
    def __add__(self, vect2: object):
        result = []
        assert len(self._vect) == len(vect2._vect)
        for item in range(len(self._vect)):
            result.append(self._vect[item] + vect2._vect[item])
        return Vector(result)
    
    def magnitude(self):
        squaresum = 0
        for item in self._vect:
            squaresum = item**2 + squaresum
        return math.sqrt(squaresum)
        
    
vec1 = Vector([4,5,6,7])
vec2 = Vector([1,2,3,4])
print(vec1 + vec2)
vec3 = vec1 + vec2
print(vec3.magnitude())