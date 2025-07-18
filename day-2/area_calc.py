class Area:
    def __init__(self):
        pass
    def area(self):
        pass
class Tringle(Area):
    def __init__(self,height,base):
        super().__init__()
        self.height = height
        self.base = base
    def area(self):
        return (1/2)*self.height * self.base
class Rectangle(Area):
    def __init__(self,height,weight):
        super().__init__()
        self.height = height
        self.weight = weight
    def area(self):
        return self.height * self.weight
a = Tringle(2,3)
print(a.area())
b = Rectangle(4,7)
print(b.area())