# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is moving."
    
# Child classes
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # Calls the constructor of the parent class
        self.breed = breed

    def move(self):
        return f"{self.name} is running."# Overriding the parent class method
    
class Fish(Animal):
    def __init__(self, name, species):
        super().__init__(name) # Calls the constructor of the parent class
        self.species = species

    def move(self):
        return f"{self.name} is swimming."# Overriding the parent class method