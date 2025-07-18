class Shape:
    def area(self):
        return "undefined"
class Rectangle(Shape):
    def __init__(self,height,width):
        super().__init__()
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
shapes = [Rectangle(2,3), Circle(5)]
for shape in shapes:
    print(shape.area())