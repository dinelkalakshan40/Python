class Phone:
    name = ""
    age = 25

    def say(self):
        print("hello")
Phone1 =Phone()
Phone1.say()

#__init__ method

class Student:
    name = "dinelka"
    age = 20

    def __init__(self,name,age):
        self.age=age
        self.name =name



studnet1 = Student("kamai",25)
print(studnet1.name)
print(studnet1.age)
studnet2 = Student("sdsd",23)
print(studnet2.name)
print(studnet2.age)

class Dog:
     attr1 = "kaizer"

     def __init__(self,name):
         self.name = name

dag1 = Dog("toomy")
dag2 = Dog("defwe")
print(dag1.name)
print(dag2.name)
