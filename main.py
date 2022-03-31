#Objects in Python
#Python is an object-oriented language and classes form the basis for all data types: int class for integers, float class for floating point values
#and the str class for character strings

#Unlike Java and C++, Python is a dynamically typed language as there is no advance declaration associating an identifier with a particular data type.

#The process of creating a new instance of a class is known as instantiation, in general, the syntax for instantiating an object is to invoke the constructor of a class.

#For example, if there were a class named Widget, we could create an instance of that class using a syntax such as w = Widget(), assuming that the constructor does not require any parameters. If the constructor does require parameters, we might use a syntax such as Widget(a,b,c) to construct a new instance.

#Another way to indirectly create a new instance of a class is to call a function that creates and returns such instance, for example, python has a built in function name sorted, that takes a sequence of comparable elements as a parameter and returns a new instance of the list class containing those elements in sorted order. 

#Calling methods

#Python supports traditional functions that are invoked with a syntax such as sorted(data), in which case data is a parameter sent to the function.

#Python's classes may also define one or more methods (also known as member functions), which are invoked on a specific instance of a class using the dot operator. For example, Python's list class has a method named sort that can be invoked with a syntax such as data.sort().
#This particular method rearranges the contents of the list so that they are sorted.
#The expression on the left of the doy identifies the object upon which the method is invoked. Often this will be an identifier (data) but we can use the dot operator to invoke a method upon the immediate result of some other operation. For example, if response identifies a string instance, the syntax response.lower().startswith('y') first evaluates the method call
# response.lower(), which itself returns a new string instance, and then the startswith('y') method is called on the intermediate string.

#When using a method of a class, it is important to understand its behavior. Some methods return information about the state of an object, but do not change that state. These are known as accesors.

#Other methods, such as the sort method of the list class, do change the state of an object. These methods are known as mutators or update methods

#Python's built in classes

#bool, a boolean value
# int, an integer
# float, floating point number
# list, mutable sequence of objects
# tuple, immutable sequence of objects
# str, character string
# set, unordered set of distinct objects 
# frozenset, immutable form of set class
# dict, associative mapping or dictionary

#   The bool Class
#The bool class is used to manipulate logical (boolean) values: True or False. The default constructor, bool() returns False

#   The int class
#the int and float classes are the primary numeric types in python, the int class is designed to represent integer values with arbitrary magnitude. The integer constructor int() returns 0 by default

#The float class is the sole floating point type in python, using fixed precision representation. The constructor form of float( ) returns 0.0

#Sequence types: the list, tuple and str classes
 #The list, tuple, and str classes are sequence types in Python, representing a collection of values in which the order is significant

 #The list class is the most general,representing a sequence of arbitrary objects (akin to an “array” in other languages).

#The tuple class is an immutable version of the list class, benefiting from a streamlined internal representation 

#The str class is specially designed for representingan immutable sequence of text characters.
''''
tup = (12,)
print('The first tupple is : {}'.format(tup))
'''

#The set and frozenset classes
'''
Python's set class represents the mathematical notion of a set, namely a collection of elements, without duplicates, and without an inherent order to those elements. The major advantage of using set, opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. This is based on a data structure known as hash table. 

However, there are two important restrictions due to the algorithmic underpinnings. The first is that the set does not maintain the elements
in any particular order. The second is that only instances of immutable types can be added to a Python set. Therefore, objects such as integers, floating-point numbers, and character strings are eligible to be elements of a set.
'''
{'red','green'} #set
{} #empty dictionary set
set() #empty set

set( 'hello' ) #produces { h , e , l , o }

#The dict class
'''
Represents a dictionary or mapping, from a set of distinct keys associated to values. For example, a dictionary might map from unique student ID
numbers, to larger student records (such as the student’s name, address, and course grades). Python implements a dict using an almost identical approach to that of a set, but with storage of the associated values.

A dictionary literal also uses curly braces, and because dictionaries were introduced in Python prior to sets, the literal form { } produces an empty dictionary.
A nonempty dictionary is expressed using a comma-separated series of key:value pairs. 

For example, the dictionary { ga : Irish , de : German } maps
ga to Irish and de to German.

'''
