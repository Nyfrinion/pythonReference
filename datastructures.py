import algorithms
import memory
#DATA STRUCTURES
#data structures are constructs that store and organize data in memory
#so that it can be used effeciently
algorithms # more details-->
memory # more details-->

#   Linear Data Structures
#elements are arranged sequentially. 
# Array
#arrays vs lists: 
#pythons list is sort've like its native type for arrays; it has dynamic size
#and can contain a variety of datatypes. Its indexed and ordered.
my_list = [1, "apple", 3.5, True]
my_list.append()
my_list.remove()
#a typical array requires homogenous datatypes; making it more memory effecient and quicker
#an array module must be imported to use this structure
#arrays don't support as many operations as lists apparently
import array
int_array = array.array('i', [1, 2, 3, 4]) #the i is defining the datatype
int_array.append()
int_array.remove()

# Linked List
# a linked list is a data structure made up of nodes; 
# each node contains data and a pointer to the next node
# so funnily a linked list is has non-contigous memory storage unlike lists and arrays
# head and tail refer to the first and last nodes
# linked lists are easily resizable; but access is O(n) complexity; arrays/lists are O(1)
linkedlist_example # more details-->

# Stack
# stack follows LAST IN FIRST OUT principle; think like a stack of pancakes
# operations are push, pop, peek/top, isEmpty, size
# LIFO, at least in this case, means no random access
stack_example # more details-->

# Queue
# queue follow FIRST IN FIRST OUT; think like a rollercoaster line
# operations are enqueue, dequeue, peek/front, isEmpty, size
# FIFO, at least in this case, means no random access
queue_example # more details-->


#   Non-Linear Data Structures
#elements are arranged in a hierarchical or interconnected way
# Trees
#Binary Tree:
binarytree_example # more details-->

#Binary Search Tree:
binarysearchtree_example # more details-->

#Full Binary Tree:
fullbinarytree_example # more details-->

#Complete Binary Tree:
completebinarytree_example # more details-->

#Balanced Tree:
balancedtree_example # more details-->

#Unbalanced Tree:
unbalancedtree_example # more details-->


# Graphs
#Directed Graph:
directedgraph_example # more details-->

#Balanced Tree:
undirectedgraph_example # more details-->

#Unbalanced Tree:
spanningtree_example # more details-->

#Graph Representation
#Adjacency List:
directedgraph_example # more details-->

#Adjacency Matrix:
adjacencymatrix_example # more details-->

# Heaps
heap_example # more details-->

# Hash Table
hashtable_example # more details-->
