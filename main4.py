'''
Object-Oriented Programming

The main actors in the object-oriented paradigm are called objects, each 
object is an instance of a class. Each class presents to the outside world
a concise and consistent view of the objects that are instances of this class.

The class definition typically specifies instance variables, also known as data members, that the object contains, as well as the methods, also known as member functions, that the object can execute.
'''

'''
OO Design Goals
Software implementations should achieve robustness, adaptability and reusability.

Every good programmer wants to develop software that is correct, which means that a program produces the right output for all the anticipated inputs in the program’s application. In addition, we want software to be robust, that is, capable of handling unexpected inputs that are not explicitly defined for its application. 

Modern software applications, such as Web browsers and Internet search engines, typically involve large programs that are used for many years. Software, therefore, needs to be able to evolve over time in response to changing conditions in itsenvironment. Thus, another important goal of quality software is that it achieves adaptability (also called evolvability). Related to this concept is portability...

Going hand in hand with adaptability is the desire that software be reusable, that is, the same code should be usable as a component of different systems in various applications.

'''

#Object-Oriented Design Principles

#Modularity, Abstraction, Encapsulation
'''
Modularity refers to an organizing principle in which different components
of a software system are divided into separate functional units.

The notion of abstraction is to distill a complicated system down to its most fundamental parts. Typically, describing the parts of a system involves naming them and explaining their functionality. Applying the abstraction paradigm to the design of a data structure gives rise to abstract data types (ADTs). An ADT is a mathematical model of a data structure that specifies the type data stored, the operations supported on them and the types of parameters of the operations. 

We will typically refer to the
collective set of behaviors supported by an ADT as its public interface.

Python supports abstract data types using a mechanism known
as an abstract base class (ABC).

Encapsulation 
Different components of a software system should not reveal the internal details of their respective implementations. One of the main advantages of encapsulation is that it gives one programmer freedom to implement the details of a component, without concern that other programmers will be writing code that intricately depends on those internal decisions.

we will adhere to the principle of encapsulation, making
clear which aspects of a data structure are assumed to be public and which are assumed to be internal details. With that said, Python provides only loose support for encapsulation. By convention, names of members of a class (both data members and member functions) that start with a single underscore character (e.g., secret) are assumed to be nonpublic and should not be relied upon.
'''
#Design Patterns

'''
Describes a solution to a typical software design problem, a pattern provides a general template for a solution that can be applied in many different situations

'''

#Software Development

#Traditional software development involves several phases. Three major steps are:

#Design, Implementation, Testing and Debugging

"""
Design 
For OOP, the design step is the most important, for it is in the design step that we decide how to divide the workings of our program into classes and decide how these classes will interact, what data each will store and what actions each will perform.

-Responsibilities: Divide the work into different actors, each with a different responsibility.
-Independence: Define the work for each class to be as independent from other classes as possible.
-Behaviors: Define the behaviors for each class carefully and precisely, so that the consequences of each action performed by a class will be understood by other classes that interact with it.  

Defining the classes, together with their instance variables and methods, are key to the design of an object-oriented program.

"""

#Testing and Debugging.

#Testing is the process of experimentally checking the correctness of a program, while debugging is the process of tracking the execution of a program and discovering errors in it. 

#Class Definitions 
'''
A class serves as the primary means for abstraction in OOP. 
Set of Behaviors -> member functions or methods
Attributes -> fields, instance variables or data members

'''

#The self identifier
'''
self identifies the instance upon which a method is invoked. For
example, assume that a user of our class has a variable, my card, that identifies an instance of the CreditCard class. When the user calls my card.get balance( ), identifier self, within the definition of the get balance method, refers to the card known as my card by the caller. The expression, self. balance refers to an instance variable, named balance, stored as part of that particular credit card’s state.
'''

class CreditCard:
    #A consumer credit card
    #The __init__ function is called every time an object is created from a #class. The __init__ method lets the class initialize the object's attributes.
    def __init__(self, customer, bank, acnt, limit):
        #Creates a new credit card instance

        #The initial balance is zero
        '''
        customer the name of the customer (e.g., 'John Smith')
        bank the name of the bank (e.g., 'California Savings')
        acnt the account identifier (e.g., '5391 0375 9387 5309')
        limit credit card limit (measured in dollars)
        '''

        def get_customer(self):
            #Return name of the customer
            return self._customer
        def get_bank(self):
            #Return the banks name
            return self._bank
        def get_account(self):
            #Return the card identifying number stored as string
            return self._account
        def get_limit(self):
            #Return current credit limit
            return self._limit
        def get_balance(self):
            #return current balance
            return self._balance
        def charge(self, price):
            #Charge given price to card, assuming sufficient credit limit
            #Return true if charge was processed; False if charge was denied
            if price + self._balance > self._limit: #if charge would exceed limit, can't accept charge
                return False
            else:
                self._balance += price
                return True
        
        def make_payment(self, amount):
            #Process customer payment that reduces balance
            self._balance-=amount


'''
The Constructor
A user can create an instance of the CreditCard class using a syntax as:
cc = CreditCard( John Doe, 1st Bank , 5391 0375 9387 5309 , 1000)

Internally, this results in a call to the specially named init method that
 serves as the constructor of the class. Its primary responsibility is to 
 establish the state of a newly created credit card object with 
 appropriate instance variables. In the case of the CreditCard class, 
 each object maintains five instance variables, which we name: 
 customer, bank, account, limit, and balance. 
'''

#Encapsulation
'''
A single leading underscore in the
name of a data member, such as balance, implies that it is intended 
as nonpublic. Users of a class should not directly access such member

'''

"""
We note that in the command, self. balance -= amount, the expression
self._balance is qualified with the self identifier because it represents an instance variable of the card, while the unqualified amount represents the local parameter.
"""
if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Bowman', 'California Federal', '3845 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =',wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
