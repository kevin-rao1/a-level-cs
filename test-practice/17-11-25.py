class Wagon:
    def __init__(self, name:str, weight:int, noofwheels:int):
        self._name = name
        self._weight = weight
        self._noofwheels = noofwheels
    
    def __str__(self):
        return f"<Wagon: {self._name}>"

class OpenWagon(Wagon):
    def __init__(self, name:str, weight:int, noofwheels:int):
        super().__init__(name, weight, noofwheels)
    
    def __str__(self):
        return f"<Open Wagon: {self._name}>"

class ClosedWagon(Wagon):
    def __init__(self, name:str, weight:int, noofwheels:int, height:int, noofdoors:int):
        super().__init__(name, weight, noofwheels)
        self._height = height
        self._noofdoors = noofdoors
    
    def __str__(self):
        return f"<Closed Wagon: {self._name}>"

class Siding:
    def __init__(self):
        self._top = -1
        self._wagons = []
    
    def push(self, wagon):
        self._top += 1
        self._wagons[self._top] = wagon
    
    def pop(self):
        if self._top == -1:
            raise IndexError
        else:
            wagon = self._wagons[self._top]
            self._wagons[self._top] = None
            self._top -= 1
            return wagon
    
    def __str__(): 
        return f"Siding with {str(self._wagons)}"

class Yard:
    def __init__(self, noofsidings):
        self._sidings = [None for i in range(noofsidings)]
        for siding in self._sidings:
            siding = Siding()

    
    def __str__():
        return f"Yard {str([str(siding) for siding in self._sidings])}"
    
def test():
    belgrrrade = Yard(6)
    Thomas = ClosedWagon("Thomas", 5, 6, 7, 8)
    belgrrrade._sidings[1].push(Thomas)
    print(belgrrrade)

if __name__ == "__main__":
    test()
