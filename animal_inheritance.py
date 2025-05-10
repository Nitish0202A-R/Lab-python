class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks.")

class Puppy(Dog):
    def weep(self):
        print(f"{self.name} weeps softly.")

my_puppy = Puppy("Tommy")
my_puppy.speak()
my_puppy.bark()
my_puppy.weep()
