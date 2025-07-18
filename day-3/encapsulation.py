class Protected:
    def __init__(self):
        self._age = 30
class Subclass(Protected):
    def display_age(self):
        print(self._age)

obj = Subclass()
obj.display_age()


#polymerphism
def add(a,b):
    return a + b
print(add(3,6))
print(add("hello","world"))
print(add([1,3],[2,7]))