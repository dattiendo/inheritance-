class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Child(Person): 
    def __init__(self, name, age):
        super().__init__(name, age)

person = Person("dat", 19)
child = Child("dat jr", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)