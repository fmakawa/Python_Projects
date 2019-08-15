#----------------------------------------------------------------------------#
                #Encapsulation
#----------------------------------------------------------------------------#
#Hiding Information: Encapsulation is a mechanism that restricts direct access
#to objects data and methods. But at the same time, it facilitates operation
#on that data (objects methods)

#----------------------------------------------------------------------------#
                #Public Instance Variables
#----------------------------------------------------------------------------#


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

tk = Person('Tkay')
print (tk.first_name) #=> TK

class Person:
    first_name = "Tkzee"
tkzee = Person()
print(tkzee.first_name) #+> Tkzee

#interesting thing about the public
#part is that we can manage the variable value. What do I mean
#by that? Our object can manage its variable value: Get and
#Set variable values.
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

tkza = Person('TK')
tkza.first_name = 'Kaio'
print(tkza.first_name) # => Kaio

#We just set another value (kaio) to the first_name instance variable
#and it updated the value. Simple as that. Since it'/s a public
#variable, we can do that

#----------------------------------------------------------------------------#
                #Non-Public Instance variable
#----------------------------------------------------------------------------#

#We dont use the term private here, since no attribute is really private in
#Python without a generally unnecessary amount of work PEP8
#As the public instance variable , we can define the non-public instance
#variable both within the constructor method or within the class. The syntax
#difference is: for non-public instance variables , use an underscore (_) before
#the variable name.

class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email  #non-public variable

hideki = Person ("Hideki","hideki@email.com")
print (hideki._email) #hideki@email.com

#We can access and update it. Non-public variables are just a convention and
#should be treated as a non-public part of the API.
#Example of Proper Use of Non-Public Variable
class Person:
    def __init__ (self, first_name, email):
        self.first_name = first_name
        self._email = email

    def update_email(self, new_email):
        self._email = new_email

    def email(self):
        return self._email

raz = Person ("Raz", "raz@email.com")
print (raz.email()) #+> raz@email.com
raz._email = "newer_raz@email.com"
print (raz.email()) #=> newer_raz@email.com
raz.update_email("evennewer_raz@email.com")
print (raz.email())#=> evennewer_raz@email.com

#We initiated a new object with first_name TK and email tk@mail.com
#Printed the email by accessing the non-public variable with a method
#Tried to set a new email out of our class
#We need to treat non-public variable as non-public part of the API
#Updated the non-public variable with our instance method
#Success! We can update it inside our class with the helper method

#Public Method
#With public methods, we can also use them out of our class:
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def show_age(self):
        return self._age

#test
ray = Person("Ray",42)
print (ray.show_age()) #42

#Non-Public Method
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def _show_age(self):
        return self._age

#test

kajun = Person("Kajun", 55)
print (kajun._show_age()) #55
#We can access and update it. Non-public methods are just a convention and
#should be treated as a non-public part of the API.
#Example of Use:

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def show_age(self):
        return self._get_age()

    def _get_age(self):
        return self._age

jon = Person("Jon", 27)
print (tk.show_age()) #27

#Encapsulation Summary
#With encapsulation we can ensure that the internal representation of the
#object is hidden from the outside.

#----------------------------------------------------------------------------#
                #More Explanations
#----------------------------------------------------------------------------#
# Public vs Non-Public
