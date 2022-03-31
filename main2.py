#Exception Handling:
"""
Exceptions are unexpected events that occur during the execution of a program. 
It might result from a logical error or an unanticipated situation. In
Python, exceptions (also known as errors) are objects that are raised (or thrown) by
code that encounters an unexpected circumstance.
"""
#try-except control structure:

from unittest import result


x=int(input("Enter a value for x: "))
y=int(input("Enter a value for y: "))

try:
    ratio=x/y
except ZeroDivisionError: #Common exception class in python (page 33)
    print('You cant divde x with 0')


try:
    fp=open('sample.txt')
except IOError as e: #Raised upon failure of I/O operation (e.g., opening file)
    print('Unable to open the file ',e)
    #In this case, the name, e, denotes the instance of the exception that was thrown,
    #and printing it causes a detailed error message to be displayed (e.g., 'file not found').
    

"""
A try statement may handle more than one type of exception, for example:
age = int(input( Enter your age in years: ))
This command could fail for a variety of reasons, the call to input will raise an EOFError if the console input fails
If the call to input completes successfully, the
int constructor raises a ValueError if the user has not entered characters representing a valid integer. If we want to handle two or more types of errors in the same
way, we can use a single except-statement, as in the following example:
"""

#age = int(input('Enter your age in years: '))
age=-1 #an initially invalid choice
while age <= 0:
    try:
        age = int(input('Enter your age in years: '))
        if age <= 0:
            print('Your age must be positive')
    #EOFError Raised if "end of file" reached for console or file input        
    except(ValueError,EOFError): #ValueError: Raised when parameter has invalid value
        print('Invalid Response')


age=-10 # an initially invalid choice
while age <= 0:
    try:
        age = int(input('Enter your age in years: '))
        if age <= 0:
            print( 'Your age must be positive ')
    except ValueError:
        print( 'That is an invalid age specification ')
    except EOFError:
        print('There was an unexpected error reading input.' )
        raise # lets re-raise this exception

"""
Generators
    However, the most convenient technique for creating iterators in Python
is through the use of generators. A generator is implemented with a syntax that
is very similar to a function, but instead of returning values, a yield statement is
executed to indicate each element of the series. 
"""

#For example, the number 100 has factors 
# 1, 2, 4, 5, 10, 20, 25, 50, 100. 
# A traditional function might produce and return a list 
# containing all factors, implemented as:

def factors(n): #traditional function that computes factors
    results=[]  #store factors in a new list
    for k in range(1,n+1):  #
        if n % k == 0:  #divides evenly, thus k is a factor
            results.append(k)   #add k to the list of factors
    return results      #return the entire list


#In contrast, an implementation of a generator for 
#computing those factors could be implemented as follows:

def factors(n): # generator that computes factors
    for k in range(1,n+1):
       if n % k == 0: # divides evenly, thus k is a factor
          yield k # yield this factor as next result

"""
use of the keyword yield rather than return to indicate a result. 
This indicates to Python that we are defining a generator, rather
than a traditional function. It is illegal to combine yield and 
return statements in the same implementation
"""

#Simulataneous assignments
def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b=b,a+b

"""
# Yield is a keyword in Python that is used to return from a function without 
# destroying the states of its local variable and when the function is called, the execution 
# starts from the last yield statement. Any function that contains a yield keyword is termed 
# a generator. Hence, yield is what makes a generator."""  """
"""

#First-Class objects
#First class objects are instances of a type that can be assigned to an identifier, passed as a parameter or returned by a function. 

scream = print #assign name 'scream' to the function denoted as 'print'
scream('Hello') #call that function
