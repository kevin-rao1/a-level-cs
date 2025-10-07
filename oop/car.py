class Car:
    def __init__(self, n, f, m, c):
        self._colour = c
        self._mass = m
        self._fuel_type = f
        self.name = n

    def repaint(self, new_colour):
        old_colour = self._colour
        self._colour = new_colour
        print(f"Repainted from {old_colour} to {new_colour}.")

    def debloat(self, mass_delta):
        self._mass = self._mass + mass_delta
        print(f"Car mass changed by {mass_delta} to {self._mass}")