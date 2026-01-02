# Inheritance : when one class derives the properties & method of another class.
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped")
class ToyotaCar(Car): # inheritance(Car)
   def __init__(self, name):
       self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius") 

#print(car1.name)
#print(car1.start())
print(car1.color)



""" INHERITANCE TYPES 
1. Single Inheritance
2. Multi_level Inheritance
3. Multiple Inheritance """