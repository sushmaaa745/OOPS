###Object Oriented Programming 

''
#class - defines the structure and behavior (attributes and methods) that the objects created from the class will have.

class Bike:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def ride(self):
        return "Vroom!"

#object - instance of class
my_bike = Bike("Yamaha", "MT-07", "2021")

''

''
#instance variable

class Bike:
    total_bikes = 0  
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model  

    def increment_total_bikes(self): 
        Bike.total_bikes += 1  
bike1 = Bike("Yamaha", "MT-07")
print(Bike.total_bikes) 
bike1.increment_total_bikes()
print(Bike.total_bikes)  

''

#Normal method

class Bike:
    def ride(self):  
        print("It is a normal method")  

obj = Bike() 
obj.ride() 

#class methods
class Bike:
    total_bikes = 0
    @classmethod
    def increment(cls):
        cls.total_bikes += 1
bike1 = Bike()
bike2 = Bike()
print(Bike.total_bikes)
Bike.increment()
print(Bike.total_bikes)
Bike.increment()
print(Bike.total_bikes)

#Static method

class Car:
    @staticmethod
    def make_sound():
        return "Vroom!"
    @staticmethod
    def info():
        return "THIS IS A CAR"

''

''
#int method

class Bike:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
#str method
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Car: {self.brand} {self.model}"
#new method
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Car: {self.brand} {self.model}"
    
    def start_engine(self):
        return "Engine Started!"
    
''

''

#constructor and deconstructor
class Bike:
    def __init__(self):
        print("CONSTRUCTOR CALLED")

    def __del__(self):
        print("DECONSTRUCTOR CALLED")

obj = Bike()  
del obj

''

''
#constructor with default arguments and constructor with arguments , without arguments also
class Car:
    def __init__(self):
        print("without arguments called")
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print("arguments called")
    def __init__(self, brand="Toyota", model="Camry"):
        self.brand = brand
        self.model = model
        print("Default arguments called")
''

''
##Method with argument

class Car:
    def drive(self, speed, distance):
        print(f"Driving at {speed} mph for {distance} miles.")


#pass object as argument
class Car:
    def __init__(self, speed):
        self.speed = speed

    def increase_speed(self, other):
        self.speed += other.speed
#Object as an return type
class Car:
    def __init__(self, speed):
        self.speed = speed

    def increase_speed(self):
        self.speed += 1
        return self
#method overloading
class Car:
    def my_method(self, arg1, arg2=0):
        print(f"arg1: {arg1}, arg2: {arg2}")

''

''
#data encapsulation
class Bike:
    def __init__(self):
        self.__speed = 1
    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        self.__speed = speed
obj = Bike()
print(obj.get_speed())
''

''
#data abstraction
class Bike:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price
    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid Price")
''

''
#data hiding
class Bike:
    def __init__(self):
        self.__hidden_var = 0
    def get_hidden_var(self):
        return self.__hidden_var
    def set_hidden_var(self, value):
        self.__hidden_var = value
obj = Bike()
obj.set_hidden_var(x)
print(obj.get_hidden_var()) 
''
 













    
    







