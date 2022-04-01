#Algorithm Analysis

#A data structure is a systematic way of organizing and accessing data, and
#An algorithm is a step by step procedure for performing some task in a finite amount of time.

#Running time is a natural measure of 'goodness', computer solutions should run as fast as possible.

#Experimental Studies

"""
If an algorithm has been implemented, we can study its running time by executing it on various test inputs and recording the time spent during each execution. A simple approach for doing this in python is by using the time function of the time module
"""

from re import A
from time import time

start_time = time() #record the starting time
#run algorithm
end_time = time() #record the ending time

elapsed = end_time - start_time #compute the elapsed time

#Functions used
'''
The constant function 
    f(n) = c

The constant function is useful in algorithm analysis because it characterizes the number of steps needed to do a basic operation on a computer: adding two numbers, assigning a value to some variable...
'''

"""
The Logarithm Function
    f(n) = logb (n), for some constant b > 1
            x = logb (n) if and only if b^x = n
"""

"""
The N-Log-N function
    f(n) = n log n

        That is the function that assigns to an input n the value of n times the logarithm base-two of n
"""

"""
The Quadratic Function
    f(n) = n^2

    Given an input value n, the function f assigns the product of n with itself
    The main reason why the quadratic function appears in the analysis of algorithms is that there are many algorithms that have nested loops, where the inner loop performs a linear number of operations and the outer loop is performed a linear number of times. Thus, the algorithm performs n * n operations
"""

"""
The Cubic Function and other Polynomials
    f(n) = n^3

Polynomials
    f(n) = a0 +a1n+a2n2 +a3n3 +···+adnd,
where a0,a1,...,ad are constants, called the coefficients of the polynomial, and ad= 0. Integer d, which indicates the highest power in the polynomial, is called the degree of the polynomial.
"""

"""
The Exponential Function
    f(n) = b^n
    b is a positive constant, called base
    n is the exponent
"""

"""
Ideally, we would like data structure operations to run in times proportional to the constant or logarithm function, and we would like our algorithms to run in linear or n-log-n time. Algorithms with quadratic or cubic running times are less practical, and algorithms with exponential running times are infeasible for all but the smallest sized inputs.
"""

#In algorithm analysis, we focus on the growth rate of the running time as a function of the input size n, taking a “big-picture” approach. For example, it is often enough just to know that the running time of an algorithm grows proportionally to n.

def findMax(data):
    #Return the maximum element from a nonempty list
    biggest = data[0] #the initial value to beat
    for val in data: #for each value in data list
        if val > biggest:
            biggest = val
    return biggest

#This is a classic example of an algorithm with a running time that grows proportional to n, as the loop executes once for each data element

"""
The Big-O notation
Let f(n) and g(n) be functions mapping positive integers to positive real numbers. We say that f(n) is O(g(n)) if there is a real constant c > 0 and an integer constant n0 >=1 such that 
        f(n) ≤ cg(n), for n ≥ n0
This definition is often referred to as the big O notation.

The big-Oh notation allows us to say that a function f(n) is “less than or equal to” another function g(n) up to a constant factor and in the asymptotic sense as n grows toward infinity

"""

#The Big-O notation is used widely to characterize running times and space bounds in terms of some parameter n, which varies from problem to problem, but is always defined as a chosen measure of the 'size' of the problem.

"""
For example, if we are interested in finding the largest element in a sequence, as with the find_max algorithm, we should let n denote the number of elements in that collection. Using the big-Oh notation, we can write the following mathematically precise statement on the running time of algorithm find_max for any computer.

The algorithm, find max, for computing the maximum element
of a list of n numbers, runs in O(n) time
"""

#Big-Theta
#In addition, there is a notation that allows us to say that two functions grow at the same rate, up to constant factors

"""
Asymptotic Analysis is the big idea that handles above issues in analyzing algorithms. In Asymptotic Analysis, we evaluate the performance of an algorithm in terms of input size (we don't measure the actual running time)We calculate, how the time (or space) taken by an algorithm increases with the input size.

The observation above raises the issue of what constitutes a “fast” algorithm. Generally speaking, any algorithm running in O(nlogn) time (with a reasonable constant factor) should be considered efficient. Even an O(n^2)-time function may be fast enough in some contexts, that is, when n is small. But an algorithm running in O(2^n) time should almost never be considered efficient
"""

#Examples of Algorithm Analysis

#Constant-Time Operations

#Given an instance, named data, of the python list class, a call to the function , len(data), is evaluated in constant time.
#This is a very simple algorithm because the list class maintains, for each list, an instance variable that records the current length of the list. This allows it to immediately report that length, rather than take time to iteratively count each of the elements in the list.
# Using asymptotic notation, we say that this function runs in O(1) time; that is, the running time of this function is independent of the length, n, of the list. #

#data[j] is evaluated in O(1) time for a python list
#a return statement in python uses O(1) time 

#A Quadratic time algorithm 
"""
Our first algorithm for computing prefix averages, named prefix_average1, computes every element of A separately, using an inner loop to compute the partial sum

"""



def prefix_average1(S):
    #Return list such that, for all j, A[j] equals average of S[0],...,S[j]
    n = len(S) #n equals the length of S (constant time)
    A = [0]*n #creates new list of zeros (O(n) time)
    for j in range(n): #loop controlled by counter j, executed n times (O(n) time)
        total = 0   #begin computing S[0]+ ...+S[j]
        for i in range(j+1): #loop controlled by counter i, executed j+1 times, depending on the current value of the outer loop counter j, (O(n^2) time)
            total += S[i]
        A[j] = total / (j+1)    #record the average
    return A

"""
The running time of implementation prefix_average1 is given by the sum of three terms: O(n^2)
"""

#A linear-time algorithm

"""
Our final algorithm, prefix averages3, we are interested in computing, for each j, the prefix sum S[0] + S[1] + ··· + S[ j], denoted as total in our code, so that we can then compute the prefix average A[j] =total / (j + 1)However, there is a key difference that results in much greater efficiency.

"""

def prefix_average3(S):
#Return list such that, for all j, A[j] equals average of S[0], ..., S[j]
    n = len(S)
    A = [0]*n # create new list of n zeros
    total = 0 # compute prefix sum as S[0] + S[1] + ...
    for j in range(n): #execute n times
        total += S[j] # update prefix sum to include S[j]
        print(total)
        A[j] = total / (j+1) # compute average based on current sum
        print(A[j])
    print(A)

prefix_average3([8,16,24])

#running time: O(n)

#Three-Way Set Disjointness
def disjoint1(A,B,C):
    #return true if there is no element common to all three lists
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False #common value found
    return True #if this point is reached, sets are disjoint


A=[11,2,3]
B=[4,11,6]
C=[11,12,13]
print(disjoint1(A,B,C))

"""
This simple algorithm loops through each possible triple of values from the
three sets to see if those values are equivalent. If each of the original sets has size n, then the worst-case running time of this function is 
O(n^3)
"""
#Improvement upon asymptotic performance:

def disjoint2(A,B,C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c: #(and thus a==b==c)
                        return False
    return True
"""
The worst case running time for disjoint2 is O(n^2)
"""

#Element Uniqueness: We are given a single sequence S with n elements asked
#whether all elements of that collection are distinct form each other
#first solution: iterative algorithm

def unique1(S):
    #return true if there are no duplicate elements in sequence S
    n = len(S)
    for j in range(n): #executes n times
        #k goes from j+1 to n (which is the length of s)
        for k in range(j+1,n): #depends on j+1 from outside loop
            if S[j] == S[k]:
                print(S[j])
                print(S[k])
                return False    #found duplicate pair
    return True     #if we reach this, elements were unique



sen = [1,2,4,3,4]
print(unique1(sen))

#####################
#Using sorting as a Problem-Solving Tool

""""
An even better algorithm for the element uniqueness problem is based on using sorting as a problem-solving tool. In this case, by sorting the sequence of elements, we are guaranteed that any duplicate elements will be placed next to each other. Thus, to determine if there are any duplicates, all we need to do is perform a single pass over the sorted sequence, looking for consecutive duplicates
"""
def unique2(S):
    #return true if there are no duplicate elements in sequence s
    temp = sorted(S) #create a sorted copy of S
    print(temp)
    #j goes form 1 to the length of temp list
    for j in range(1, len(temp)):
        if S[j-1] == S[j]:
            return False    #found duplicate pair
    return True         #if we reach this, elements were unique

"""
The built in function, sorted guarantees a worst-case running time of O(nlogn). Once data is sorted, the subsequent loop runs in O(n) time, so the entire unique2 algorithm runs in O(nlogn) time.
"""
Sne=[1,24,5,2,1]
print(unique2(Sne))
