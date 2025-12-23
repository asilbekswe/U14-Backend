################################# 1. Encapsulation (Inkapsulyatsiya)
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount


    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
        

account = BankAccount("Ali")
account.deposit(1000)
account.withdraw(500)
print(account.get_balance())


################################# 2. Inheritance (Meros)

class Animal:
    def speak(self):
        print("sound")

class Dog(Animal):
    def speak(self):
        print("Woow, woow")

dog = Dog()
dog.speak()


################################   3. Polymorphism (Polimorfizm)


class Cat:
    def speak(self):
        print("Cat meows")

class Dog:
    def speak(self):
        print("Dog barks")

def animal_sound(animal):
    return animal.speak()

cat = Cat()
dog = Dog()
animal_sound(cat)
animal_sound(dog)


#################################   4. Dunder Methods (Spesial metodlar)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  
print(p3)


################################# 5. Static Method (Statik metodlar)

class Math:
    @staticmethod
    def multiply(a, b):
        return a * b

result = Math.multiply(4, 5)
print(result)

#################################   6. Class Method (Klass metodlari)

class Person:
    name = "Unknown"

    @classmethod
    def set_name(cls, name):
        cls.name = name

Person.set_name("Ali")
print(Person.name)


#################################  7. Abstraction (Abstraksiya)


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()



################################# 8. Access Modifiers (Kirish modifikatorlari)
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__salary = 50000


    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

person = Person("Ali", 18)
print(person.get_salary())
person.set_salary(60000)
print(person.get_salary())
