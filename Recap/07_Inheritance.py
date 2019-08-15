#----------------------------------------------------------------------------#
                #Inheritance: Behaviour and Characteristics
#----------------------------------------------------------------------------#

#In OOP classes can inherit common characteristics (data) and behavior
#(methods) from another class.

class Car:
    def __init__ (self, number_of_wheels, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

my_car = Car(4,6,275)
print(my_car.number_of_wheels)#4
print(my_car.seating_capacity)#6
print(my_car.maximum_velocity)#275

#we apply a parent class to the child class as a parameter. An ElectricCar class
#can inherit from our Car class.

class ElectricCar(Car):
    def __init__(self,number_of_wheels,seating_capacity,maximum_velocity,creator):
        Car.__init__(self,number_of_wheels,seating_capacity,maximum_velocity)
        self.creator = creator

my_electriccar = ElectricCar(2,3,150, "Elon Musk")
print(my_electriccar.number_of_wheels) #2
print(my_electriccar.seating_capacity) #3
print(my_electriccar.maximum_velocity) #150
print(my_electriccar.creator) #Elon Musk
