#Expressions, Operators and Precedence

#Logical operator

'''
not unary negation
and conditional and
or conditional or

The and and or operators short-circuit, in that they do not evaluate the second operand if the result can be determined based on the value of the first operand.

'''

#Equality operators

'''
is same identity
is not different identity
== equivalent
!= not equivalent

The expression a is b evaluates to True, precisely when identifiers a and b are aliases for the same object. The expression a == b tests a more general notion of equivalence. If identifiers a and b refer to the same object, then a == b should also evaluate to True. 

'''

#Comparison Operators

"""
Data types may define natural order via the following operators
< less than
<= less than or equal to
> greater than
>= greater than or equal to
"""

#Arithmetic Operators

'''
+ addition
− subtraction
multiplication
/ true division
// integer division
% the modulo operator
'''

#Bitwise operators

"""
Python provides the following bitwise operators for integers:
∼ bitwise complement (prefix unary operator)
& bitwise and
| bitwise or
ˆ bitwise exclusive-or
<< shift bits left, filling in with zeros
>> shift bits right, filling in with sign bit
"""

#Sequence Operators
'''
Each of Python’s built-in sequence types (str, tuple, and list) support the following
operator syntaxes:
s[j] element at index j
s[start:stop] slice including indices [start,stop)
s[start:stop:step] slice including indices start, start + step,
start + 2 step, . . . , up to but not equalling or stop
s+t concatenation of sequences
k s shorthand for s + s + s + ... (k times)
val in s containment check
val not in s non-containment check
'''
#Because lists are mutable, the syntax s[j] = val can be used to replace an element at a given index. Lists also support a syntax, del s[j], that removes the designated element from the list. Slice notation can also be used to replace or delete asublist

"""
Operators for Sets and Dictionaries
Sets and frozensets support the following operators:
-key in s containment check
-key not in s non-containment check
-s1 == s2 s1 is equivalent to s2
-s1 != s2 s1 is not equivalent to s2
-s1 <= s2 s1 is subset of s2
-s1 < s2 s1 is proper subset of s2
-s1 >= s2 s1 is superset of s2
-s1 > s2 s1 is proper superset of s2
-s1 | s2 the union of s1 and s2
-s1 & s2 the intersection of s1 and s2
-s1 − s2 the set of elements in s1 but not s2
-s1 ˆ s2 the set of elements in precisely one of s1 or s2

"""
'''
The most widely used behavior of dictionaries is accessing a value
associated with a particular key k with the indexing syntax, d[k]. The supported
operators are as follows:
d[key] value associated with given key
d[key] = value set (or reset) the value associated with given key
del d[key] remove key and its associated value from dictionary
key in d containment check
key not in d non-containment check
d1 == d2 d1 is equivalent to d2
d1 != d2 d1 is not equivalent to d2 '''


#Conditionals
'''
Conditional constructs (also known as if statements) provide a way to execute a
chosen block of code based on the run-time evaluation of one or more Boolean
expressions. In Python, the most general form of a conditional is written as follows:
        if first condition:
        first body
        elif second condition:
        second body
        elif third condition:
        third body
        else:
        fourth body '''

#Loops: A while loop allows general repetition based upon the repeated testing of a Boolean condition. A for loop provides convenient iteration of values from a defined series (such as characters of a string, elements of a list, or numbers within a given range)

#Syntax:

#while condition:
    #body

#The len function returns the length of a sequence such as a list or a string.

#For Loops

#Can be used on any type of iterable structure, such as a list, str, set, dict or file. General syntax:

'''
for element in iterable:
    body #body refers to element as identifier
    '''
data=[1,2,3,21,10,4]

'''
total=0
for val in data:
    total+=val
    print(total)
'''

#The loop executes once for each element of the data sequence, with the identifier, val, from the for-loop syntax assigned at the beginning of each pass to a respective element 

#finding the maximum value in a list of elements (again, admitting that Python’s built-in max function already provides this support). If we can assume that the list, data, has at least one element, we could implement this task as follows:


data1=[10,3,25,64,2]
#loop starts at start of list
biggest=data[0]
#for each value in data list
for val in data1:
    #if that value is bigger than the value before
    if val > biggest:
    #biggest is now that value
        biggest = val
#print biggest number of list
print(biggest)

#Index-based for loops: a standard idiom for looping through the series of indices
#of a dara sequence uses a syntax:

for j in range (len(data)):
    #in this case, identifier j is no an element of data-it is an integer
    #For example, we can find the index of the max element of a list as follows:
    big_index=0
    for j in range (len(data)):
        if data[j] > data[big_index]:
            big_index = j

#Break and Continue statements

"""
Python supports a break statement that immediately terminate a while or for loop
when executed within its body. More formally, if applied within nested control
structures, it causes the termination of the most immediately enclosing loop. As
a typical example, here is code that determines whether a target value occurs in a
data set:
"""
target = 12 #Number targeted
data = [1,12,345,34,1] #list
found = False #boolean value
for item in data: #for each item in the list
    if item == target: # if item[i] is the target
        found = True #boolean is true-the target was found
        break
if(found == False):
    print("No {} was found".format(target))
else:
    print("{} was found".format(target))


#Functions

def count(data,target):
    n=0
    for item in data:
        if item==target:
            n+=1
    return n

#Default parameter values
"""
Python provides means for functions to support more than one possible calling signature
Such function is said to be polymorphic. Functions can declare one or more default value for parameters, 
thereby allowing the caller to invoke a function with varying numbers of actual parameters. 
"""

def foo(a, b=15,c=27):
    #there are three parameters, the last two of which offer default values
    #A calller is welcome to send three actual parameters, as in foo(4,12,8) in which case
    #the default values are not used.

    """
    If on the other hand, the caller only sends one parameter, foo(4), the function will execute
    with parameters values a=4,b=15,c=27
    """

def range(start,stop=None, step=1):
    if stop is None:
        stop=start
        start=0

#Pythons built in functions
 #Refer to page 28 and 29 of Goodrich's book

 #The input function
year=int(input('In what year were you born? '))
print("You were born in {}".format(year))

reply=input('Enter x and y, separated by spaces: ')
pieces=reply.split() #return a list of strings, as separated by spaces
x=float(pieces[0])
y=float(pieces[1])
z=float(pieces[2])
print(x)
print(z)

#Files
#Files are typically accessed in python beginning with a call to a built in function
#named open, that returns a proxy for interactions with the underlying file. For example
#the command fp = open('sample.txt') attempts to open a file named sample.txt, returning a proxy that
#allows read-only access to the file.

"""
The open function accepts an optional second parameter that determines the
access mode. The default mode is r for reading. Other common modes are w
for writing to the file (causing any existing file with that name to be overwritten),
or a for appending to the end of an existing file.

Behaviors for interacting with a text file via file proxy (named fp)
Refer to page 32 in Goodrichs book.
"""
