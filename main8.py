#Binary Search Trees

#Binary trees are mainy used for searching and sorting as they provide a means to store data hierarchiacally. 


"""
A node based binary tree data structure which has the following properties:

-The left subtree node contains only nodes with keys lesser than the nodes key
-The right subtree of a node contains only nodes with keys greater than the nodes key

-Useful to limit the number of iterations like find, insert and update by organizing our data in this particular
structure.

-Each node in the tree can have at most 2 children. A node with 0 children is often called a leaf
-The single node at the top of the tree is called root node, typically where operations like search or insertion begin.

Each node of the tree stores a key and a value, a binary tree where nodes have both a key and a value is often 
referred to as a map or treemap
"""

#Height of a binary tree
"""
The height of a binary tree is the number of levels. For a tree a height k, here's a list of the number of nodes at each level:

Level 0: 1, Level 1: 2, Level 2: 4 (2^3)... 
Level k-1: 2^(k-1)

If the total number of nodes in the tree is N, then it follows that:
N = 1 + 2^1 + 2^2 + 2^3 + ... + 2^(k-1)

To store N records we require a balanced binary search tree (BST) of height no larger that log(N)+1. This is a very useful property, in combination with the fact that nodes are arranged in a way that makes it easy to find a specific key by following a single path down from the root.
"""

#Exercise 1: Implement a binary tree using python and show its usage with some examples

#The __init__ method is the python eq. of the c++ constructor of an OO approach, the function is called every time an object is created from a class.


from platform import node
from parso import parse


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
#Creation of objects representing each node of the above tree

node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

#Let's verify that node0 is an object of the type TreeNode and has the property key set to 3.

print(node0)
print(node0.key)

#We can connect the nodes by setting the .left and .right properties of the root node

node0.left = node1
node0.right = node2

#Now we can create a new variable tree which simply points to the root node, and use it to access all the node within the tree

tree = node0
print(tree.key) #3
print(tree.left.key) #4
print(tree.right.key) #5

#Exercise 2: Create the following binary tree using the TreeNode class defined above 

#Inconvenient to create a tree by manually connecting all the ndoes, so we use a helper function which can convert a tuple with the structure (left_subtree, key, right_subtree) (where left_subtree and right_subtree are themselves tuples) into binary tree

tree_tuple = ((1,3,None), 2, ((None,3,4), 5, (6,7,8)))

def parse_tuple(data):
    #isinstance returns whether an object is an instance of a class or a subclass of thereof. It returns True if the specified object is of the specified type, otherwise False.
    #If the object is a tuple, this function will return True if the object is one of the types in the tuple. 
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node
#The parse_tuple creates a new root node when a tuple of size 3 is the input. To create left and right subtrees for the node, the parse_tuple function invokes itself. (Recursion)

#The chain of recursive calls ends when parse_tuple encounters a number or None as input. 

tree2 = parse_tuple(((1,3,None), 2, ((None,3,4), 5, (6,7,8))))
print(tree2.left.key,tree2.right.key)

#Traversing a Binary Tree

#1. Write a function to perform the inorder traversal of a binary tree
#2. Write a function to perform the preorder traversal of a binary tree
#3. Write a function to perform the postorder traversal of a binary tree

#A traversal refers to the process of visiting each node of a tree exactly once. Visiting a node generally refers to adding the node's key to a list. There are three ways to traverse a binary tree and return the list of visited keys:

#A) Inorder traversal 
"""
    1. Traverse the left subtree recursively inorder.
    2. Traverse the current node.
    3. Traverse the right subtree inorder.
"""
#B) Preorder traversal
"""
    1. Traverse the current node.
    2. Traverse the left subtree recursively preorder.
    3. Traverse the right subtree recursively preorder.

"""
