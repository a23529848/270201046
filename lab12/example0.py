class Cylinder:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def setRadius(self, r):
        self.r = r

    def setHeight(self, h):
        self.h = h

    def getRadius(self):
        return self.r

    def getHeight(self):
        return self.h

    def BaseArea(self):
        pi = 3.14
        baseArea = pi * self.r ** 2
        return baseArea

    def SurfaceArea(self):
        pi = 3.14
        surfaceArea = 2 * pi * self.r * self.h
        return surfaceArea

    def Volume(self):
        return self.BaseArea() * self.h

    def Area(self):
        return self.BaseArea() * 2 + self.SurfaceArea()


cylinder = Cylinder(3, 4)  # same cylinder but it radius changes it self

print(cylinder.Volume())

cylinder.setRadius(4)

print(cylinder.Volume())
