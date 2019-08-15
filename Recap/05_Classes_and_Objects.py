#----------------------------------------------------------------------------#
                #A LITTLE BIT OF THEORY
#----------------------------------------------------------------------------#

#Objects have data and behaviour
#Data --> Attributes
#Behaviour --> Methods

#Classes are the blue print upon which Objects are created/based on. A model.
# An oject is an instance of a Class

#----------------------------------------------------------------------------#
                # Classes and Objects
#----------------------------------------------------------------------------#

#Class
class Vehicle:
    pass

#Object

car = Vehicle()
print(car) #<__main__.Vehicle instance at 0x7fbe99bb1518>

#More Class info

class VehicleDefined01:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels= number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

# the __init__ method is a constructor method.

tesla_model_s = VehicleDefined01(4,'electric',5,250)

#Accessing the values we created
class VehicleDefined02:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels= number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    # accessing the values we created we use defined methods of what we need
    # Gets the values
    def number_of_wheels(self):
        return self.number_of_wheels
    # Sets the values
    def set_number_of_wheels(self,number):
        self.number_of_wheels= number
#This is an implementation of two methods. A getter and a setter. We can use 'decorators'
# like @property to define getters and setters
#----------------------------------------------------------------------------#
                #METHODS
#----------------------------------------------------------------------------#

class VehicleDefined03:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels= number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    # accessing the values we created we use defined methods of what we need
    # Gets the values
    @property
    def number_of_wheels(self):
        return self.number_of_wheels
    # Sets the values
    @number_of_wheels.setter
    def set_number_of_wheels(self,number):
        self.number_of_wheels= number
    #Make Noise
    def make_noise(self):
        print ("VRUUUUUUUM")

tesla_model_x = VehicleDefined03(4, 'electric', 5, 250)
print(tesla_model_x.number_of_wheels) # 4
tesla_model_x.number_of_wheels = 2 # setting number of wheels to 2
print(tesla_model_x.number_of_wheels) # 2
tesla_model_x.make_noise()
