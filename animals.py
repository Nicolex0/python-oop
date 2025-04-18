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
    
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name) # Calls the constructor of the parent class
        self.species = species

    def move(self):
        return f"{self.name} is flying."# Overriding the parent class method
    
if __name__ == "__main__":
    dog = Dog("Rex", "Golden Retriever")
    fish = Fish("Nemo", "Clownfish")
    bird = Bird("Tweety", "Canary")
    animal = Animal("Generic Animal")

    animals = [dog, fish, bird, animal] # List of animal objects

    for each_animal in animals:
        print(each_animal.move())