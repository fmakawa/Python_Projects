##### List: Collection | Array | Data Structure #####
#----------------------------------------------------------------------------#
                                #LISTS
#----------------------------------------------------------------------------#
my_integers = [1,2,3,4,5]
# Remember lists have indeces and the 1st element has an index value of 0.
#for example
#Array  = [5,7,1,3,4]
#Index  = [0,1,2,3,4]

#Lists with Integers
my_integers = [5,7,1,3,4]
print (my_integers[4]) #4
print (my_integers[1]) #7
print (my_integers[0]) #5

#Lists with floating numbers
my_float = [1.2,4.55,68, 56.89,12.55]
print(my_float[3])#56.89
#lists with strings
relatives_names = [
"Lynn",
"Chi",
"Ngaa",
"Tanatsa",
"Kudzai",
]

print(relatives_names[3]) #Tanatsa

#Adding to Lists
bookshelf = []
bookshelf.append("The Effective Engineer")
bookshelf.append("The 4 Hour Work Week")
bookshelf.append(890)

print(bookshelf[0]) #The Effective Engineer
print(bookshelf[1]) #The 4 Hour Work Week
print(bookshelf[2]) #890
print(bookshelf)
#When you print the whole list it prints in order from index [0]

#List methods
"""
'__add__',
'__class__',
'__contains__',
'__delattr__',
'__delitem__',
'__dir__',
'__doc__',
'__eq__',
'__format__',
'__ge__',
'__getattribute__',
'__getitem__',
'__gt__',
'__hash__',
'__iadd__',
'__imul__',
'__init__',
'__iter__',
'__le__',
'__len__',
'__lt__',
'__mul__',
'__ne__',
'__new__',
'__reduce__',
'__reduce_ex__',
'__repr__',
'__reversed__',
'__rmul__',
'__setattr__',
'__setitem__',
'__sizeof__',
'__str__',
'__subclasshook__',
'append',
'clear',
'copy',
'count',
'extend',
'index',
'insert',
'pop',
'remove',
'reverse',
'sort'
"""

#----------------------------------------------------------------------------#
                                #Tuple
#----------------------------------------------------------------------------#

#Exactly like a list but once created nothing can be added or removed from it.
#Its not advisable to use them but there are some scenarios
#They use rounded brackets rather than square brackets

mytuple = (1,2,"tokoloshe","i am legend", 12.3)

#any methods used like append or remove will throw an error.

#----------------------------------------------------------------------------#
                                #DICTIONARY
#----------------------------------------------------------------------------#

dictionary_example = {
"key1":"value1",
"key2":"value2",
"key3":"value3",
}

#Remember a dictionary doesn't have an index, instead it uses the keys

dictionary_tk = {
"name": "Leandro",
"nickname": "Tk",
"nationality": "Brazilian",
}

print("My name is %s" %(dictionary_tk["name"])) #Leandro
print("But you can call me %s") %(dictionary_tk["nickname"]) #Tk
print("I am %s" %(dictionary_tk["nationality"])) #Brazilian

#adding to dictionaries
dictionary_tk["age"] = 24
#When you add to a dictionary ....
print(dictionary_tk) #{'nationality': 'Brazilian', 'age': 24, 'nickname': 'Tk', 'name': 'Leandro'}
#When it prints a dictionary it prints from the highest 'index', the last in the dictionary backwards
#unlike the list which prints from index [0]

#----------------------------------------------------------------------------#
                #ITERATION: LOOPING THROUGH DATA STRUCTURES
#----------------------------------------------------------------------------#
#Iteration in Lists
bookshelf =[
"The Effective Engineer",
"The 4 Hours Work Week",
"Zero to One",
"Lean Startup",
"Hooked"
]

for book in bookshelf:
    print(book)

#Iteration in hash data structures like dictionaries
dictionary = {"some_key":"some_value"}

for key in dictionary:
    print ("%s --> %s" %(key,dictionary[key]))  #some_key --> some_value

# another way of doing it
dictionary2 = {"another_key":"another_value"}

for key,value in dictionary2.items():
    print ("%s --> %s" %(key,value))
#Note: the parameters here have been named 'key' and 'value' but they could be anything

#Now iterating a previously created dictionary - 'dictionary_tk'

for attribute, value in dictionary_tk.items():
    print("My %s is %s" %(attribute,value))
#My nationality is Brazilian
#My age is 24
#My nickname is Tk
#My name is Leandro

#How can you reverse the order dictionaries are printed? We want to start with his name
#which it the first dictionary item that was added.
