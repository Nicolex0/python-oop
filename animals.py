# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is moving."