class Animal:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)
class Lizard(Reptile):
    def __init__(self, name):
        super().__init__(name)
class Snake(Reptile):
    def __init__(self, name):
        super().__init__(name)
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
class Gorilla(Mammal):
    def __init__(self, name):
        super().__init__(name)
class Bear(Mammal):
    def __init__(self, name):
        super().__init__(name)
mammal = Mammal("dat")
print(mammal.__class__.__bases__[0].__name__)  
print(mammal.name) 
lizard = Lizard("datg")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)  
