# Module 14 -- Object-Oriented Programming

OOP organises code around objects that combine data and behaviour.

## Classes and objects

A class is a blueprint; an object is an instance of that class.

``` python
class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def introduce(self):
        print(f"I am {self.name}. My mark is {self.mark}.")

student1 = Student("Asha", 90)
student1.introduce()
```

`__init__` initialises an object. `self` refers to the current instance.

## Inheritance

A child class can reuse and extend a parent class.

``` python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

Dog().speak()
```

## Polymorphism

Different objects can provide the same method name with different
behaviour.

``` python
class Cat:
    def speak(self): print("Meow")
class Dog:
    def speak(self): print("Woof")

for animal in [Cat(), Dog()]:
    animal.speak()
```

## Encapsulation

Encapsulation keeps data and related methods together. A leading
underscore, such as `_balance`, is a convention indicating an internal
attribute.

## Try it

Create a `Book` class, add a method to display its details, then create
a child class using inheritance.
