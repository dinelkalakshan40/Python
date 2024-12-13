class Parent:

    name = "laksm"
    def music(self):
        print("listen in radio")

class Child(Parent):
    age =25;
    def music(self):
        super().music()
        print("spotify")

chil1 =Child()
print(chil1.name)
chil1.music()
print(chil1.age)

print("=================================================")

class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # From Animal
dog.walk()   # From Mammal
dog.bark()   # From Dog

