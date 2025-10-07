class Rectangle:
    def __init__(self, n, f, m, c):
        self._colour = c
        self._mass = m
        self._fuel_type = f
        self.name = n

    def repaint(self, new_colour):
        old_colour = self._colour
        self._colour = new_colour
        print(f"Repainted from {old_colour} to {new_colour}.")