# BME_ML_basic6

# Class
# Object Oriented Programming (OOP)
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
from sklearn.svm import SVC
svc = SVC()
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
from sklearn.ensemble import AdaBoostClassifier
ab = AdaBoostClassifier()

# basic class
class Car():
    def __init__(self, color):
        self.color = color
my_car = Car(color='red')
print(type(my_car))
print(my_car.color)

class Car():
    def __init__(self, color, seats, types):
        self.color = color
        self.seats = seats
        self.types = types
my_car = Car(color="red", seats = 5, types = 'Jeep')
print(my_car.color, my_car.seats, my_car.types)

your_car = Car(color="black", seats = 4, types = 'Sedan')
print(your_car.color, your_car.seats, your_car.types)

his_car = Car(color="white", seats = 9, types = 'Bus')
print(his_car.color, his_car.seats, his_car.types)


class Car():
    purpose = "Transportation" # a class attribute
    def __init__(self, color, seats, types):
        self.color = color
        self.seats = seats
        self.types = types
my_car = Car(color="red", seats = 5, types = 'Jeep')
print(my_car.color, my_car.seats, my_car.types, my_car.purpose)


class Car():
    urpose = "Transportation"
    def __init__(self, color, seats, types):
        self.color = color
        self.seats = seats
        self.types = types
    # self is mandatory
    def describe(self):
        print(f"The car is a {self.color} {self.types} with {self.seats} seats")
my_car = Car(color="red", seats = 5, types = 'Jeep')
my_car.describe()

class Circle():
    # class attribues
    pi = 3.141592
    # radius (default = 0)
    def __init__(self, radius=0):
        self.radius = radius
    def get_circumference(self):
        return 2 * self.pi * self.radius
    def get_area(self):
        return self.pi * self.radius**2
my_circle = Circle(radius=10)
print(my_circle.get_circumference())
print(my_circle.get_area())

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def print_name(self):
        print(self.first_name, self.last_name)
x = Person("Jinseok", "Lee")
x.print_name()


class Student():
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
    def print_name(self):
        print(self.first_name, self.last_name)
    def print_name_id(self):
        print(self.first_name, self.last_name, self.id)
x = Student("Jinseok", "Lee", 43)
x.print_name_id()

# class inheritance
del Student

class Student(Person):
    pass # do nothing
x = Student("Jinseok", "Lee")
print(x.first_name, x.last_name)
x.print_name()

class Student(Person):
    def __init__(self, first_name, last_name, id):
        super().__init__(first_name, last_name) # inherit from the parent class
        self.id = id # add a new attribute
    def print_name_id(self): # new method
print(self.first_name, self.last_name, self.id)





