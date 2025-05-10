class Animal:
    def __init__(self, name):  # Fixed the typo in method name
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")  # Small grammar fix

class Dog(Animal):  # Class names should start with uppercase by convention
    def bark(self):
        print(f"{self.name} barks.")

# Create an instance of Dog
my_dog = Dog("Buddy")
my_dog.speak()  # Inherited from Animal
my_dog.bark()   # Specific to Dog
