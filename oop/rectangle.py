""" Task:
Create a Rectangle class that has the following
Attributes: width, height
Methods:
get_area() # Returns the area of the rectangle
get_perimeter() # Returns the perimeter.
get_diagonal() # Returns the length of the diagonal from one corner to the opposite corner."""
class Rectangle:
    def __init__(self, w, h):
        self._width = w
        self._height = h

    def get_area(self):
        return self._width * self._height
    
    def get_perimeter(self):
        return 2 * (self._width + self._height) # add first for performance
    
    def get_diagonal(self):
        return (self._width**2 + self._height**2)**(1/2)

rectangle0 = Rectangle(5, 6)
print(f"rectangle0 has area {rectangle0.get_area()}, perimeter {rectangle0.get_perimeter()}, and diagonal {rectangle0.get_diagonal()}")
# could add more code to create new rectangles easily.