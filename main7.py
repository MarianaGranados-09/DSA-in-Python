"""
QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
"""

#We can represent the sequence of cards as a list of numbers
#Turning over a specific card is equivalent to accesing the value of the #number at the corresponding position of the list. 

#Solution: find the position of a given number in a list of numbers #arranged in decreasing order. We also need to minimize the number 
#of times we access elements from the list

#The input is a list of numbers sorted in decreasing order, for example:
# [13,11,10,7,4,3,1,0]

#The query, a number whose position in the array is to be determined

#The output, is a position of the query in the list of cards

def CardsFunction(Cards):
    query = 7
    n = len(Cards)
    for j in range(0,n):
        if Cards[j] == query:
            return j
    return 'No query found in cards'

cards = [7]
print(CardsFunction(cards))

#Analyze algorithm's complexity and identify inefficiencies

"""
For a list size of N, we access the elements form the list up to N times, thus, Bob may need to overturn up to N cards in the worst case, to find the required card.

And the process of figuring out the best algorithm to solve a given problem is called algorithm design and optimization.
"""

#Complexity and more Big O Notation Theory

"""
Complexity of an algorithm is a measure of the amount of time and/or space required by an algorithm for an input of given size, e.g. N.

The term complexity always refers to the worst-case complexity.
"""


"""
At the moment, we're simply going over cards one by one, and not even utilizing the fact that they're sorted. This is called a brute force approach.

The next best idea would be to pick a random card, and use the fact that the list is sorted, to determine whether the target lies to the left or right of it. In fact, if we pick the middle card, we can reduce the number of additional cards to be tested to half the size of the list. Then, we can simply repeat the process with each half. This technique is called binary search.
"""

#Here is how binary search can be applied to our problem
#1. Find the middle element of the list
#2. If it matches the queried number, return the middle position as the answer.
#3. If it is less than the queried number, then search the first half of the list
#4. If it is greater than the queried number, then search the second half of the list
#5. If no more elements remain, return -1.

#Implementing a binary search algorithm using for loop:

def CardsFunction(Cards):
    query = 7
    n = len(Cards)
   # [13,11,10,7,4,3,1,0,5]
    #get half of the length of the list
    middleNum = int(n/2) 
    #get the number in the middle position
    middle_of_list = Cards[middleNum]
    #print(middle_of_list)

    if middle_of_list == query:
        return 'The query is at position {}'.format(middleNum)
    if middle_of_list < query:
        #Search the first half of the list
        for j in range(0,middleNum-1):
            if Cards[j] == query:
                return 'The query is at position {}'.format(j)
    if middle_of_list > query:
        #search the second half of the list
        for k in range(middle_of_list+1, n):
            if Cards[k] == query:
                return 'The query is at position {}'.format(k)

    return -1

print(CardsFunction([13,11,10,4,7,3,1,0,5]))


from re import A
from time import time

#Binary search algorithm:

def CardsFunction(Cards):
    query = 3
    if not(Cards):
        return -1
    n = len(Cards)
   # [13,11,10,7,4,3,1,0,5]
    #get half of the length of the list
    middleNum = int(n/2) 
    #get the number in the middle position
    middle_of_list = Cards[middleNum]
    print(middle_of_list)

    if middle_of_list == query:
        return 'The query is at position {}'.format(middleNum)
    if middle_of_list < query:
        #Search the first half of the list
        for j in range(0,middleNum):
            #print(Cards[j])
            if Cards[j] == query:
                return 'The query is at position {}'.format(j)
    if middle_of_list > query:
        #search the second half of the list
        for k in range(middleNum+1,n):
            #print(Cards[k])
            if Cards[k] == query:
                return 'The query is at position {}'.format(k)
                
    return -1

start = time()
print(CardsFunction([]))
end = time()

elapsed = end - start
print(elapsed)

##Generic Binary Search

"""
Here is the general strategy behind binary search, which is applicable to a variety of problems:

1. Come up with a condition to determine whether the answer lies before, after or at a given position.
2. Retrieve the midpoint and the middle element of the list.
3. If it is the answer, return the middle position as the answer.
4. If answer lies before it, repeat the search with the first half of the list.
5. If the answer lies after it, repeat the search with the second half of the list. 
"""

#The worst case complexity or running time of binary search is O(log N), provided the complexity of the condition used to determine whether the answer lies before, after or at a given position O(1).


#######################
#Implementing a Binary search with while loop

#A nonrecursive implementation of binary search

def binary_search(data, query):
    #Return True if target is found in the given python list
    low = 0
    high = len(data)-1 
    while low <= high:
        mid = (low + high) // 2 
        if query == data[mid]:  #found a match
            return 'The query is at position {}'.format(mid)
        elif query < data[mid]: 
            high = mid - 1  #only consider values left of mid
        else:
            low = mid + 1   #only consider values right of mid
    return False    #loop ended without success


dat = [1,34,2,41,3]
#print(len(dat))
print(binary_search(dat, 41))


## Problem - Rotated Lists


'''You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list. You can assume that all the numbers in the list are unique.

Example: The list `[5, 6, 9, 0, 2, 3, 4]` was obtained by rotating the sorted list `[0, 2, 3, 4, 5, 6, 9]` 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list `[3, 2, 4, 1]`produces `[1, 3, 2, 4]`. 

"Sorted list" refers to a list where the elements are arranged in the increasing order  e.g. `[1, 3, 5, 7]`.
'''

#Input

"""
The input is a list of numbers
E.g. nums = [5,6,9,0,2,3,4] was obtained by rotating the sorted list
[0,2,3,4,5,6,9] 3 times

The output will return an int rotations, which establishes the minimum number of rotations the original list was given
"""

def Num_rotations(nums):
    n = len(nums)
    high = n-1
    low = 0

    while low <= high:
        mid = low + (high-low) // 2

        #Calculate previous and next position from mid
        prev = (mid-1+n)%n
        next = (mid+1)%n

        #checking if nums[mid] is the minimum number comparing it to nums[prev] and nums[next]

        if nums[mid] < nums[prev] and nums[mid] <= nums[next]:
            return mid #returns mid position, since nums[mid] is the minimum number in the list, this number corresponds to the min number of rotations made

        #if the unsorted part of the array was not selected:
        elif nums[mid] < nums[low]:
            high = mid-1
        elif nums[mid] > nums[high]:
            low = mid + 1
        else:
            return 0 #no rotations made


s = [15, 18, 2, 3, 6, 12]
s1 = [5, 6, 9, 0, 2, 3, 4]
s2 = [3, 2, 4, 1]
print(Num_rotations(s1))



