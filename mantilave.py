class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")

class Pet:
    def show_affection(self):
        print(f"{self.name} shows affection.")

class Dog(Animal, Pet):
    def bark(self):
        print(f"{self.name} barks.")

d = Dog("Buddy")
d.speak()
d.bark()
d.show_affection()
