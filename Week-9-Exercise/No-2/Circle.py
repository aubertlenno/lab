import math

class Circle:
    def __init__(self, r = 1.0, c = "red"):
        self.__radius = r
        self.__color = c

    def getRadius(self):
        return self.__radius
    
    def setRadius(self,r):
        self.__radius = r
    
    def getColor(self):
        return self.__color
    
    def setColor(self,c):
        self.__color = c
    
    def toString(self):
        return "Radius: " + str(self.getRadius()) + "\nColor: " + str(self.getColor())
    
    def getArea(self):
        area = (self.getRadius()**2) * math.pi
        return area