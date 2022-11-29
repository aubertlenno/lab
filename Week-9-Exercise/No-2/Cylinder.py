from Circle import Circle

class Cylinder(Circle):
    def __init__(self, r = 1.0, c = "red", h = 1):
        super().__init__(r,c)
        self.__height = h
    
    def getHeight(self):
        return self.__height
    
    def setHeight(self,h):
        self.__height = h

    def toString(self):
        return super().toString() + "\nHeight: " + str(self.getHeight())

    def getVolume(self):
        volume = super().getArea() * self.getHeight()
        return volume