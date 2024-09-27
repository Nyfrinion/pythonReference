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
#a linked list is a data structure made up of nodes; 
#each node contains data and a pointer to the next node
#so funnily a linked list is has non-contigous memory storage unlike lists and arrays
#head and tail refer to the first and last nodes
#linked lists are easily resizable; but access is O(n) complexity; arrays/lists are O(1)
linkedlist_example # more details-->

# Stack
#stack follows LAST IN FIRST OUT principle; think like a stack of pancakes
#operations are push, pop, peek/top, isEmpty, size
#LIFO, at least in this case, means no random access
stack_example # more details-->

# Queue
#queue follow FIRST IN FIRST OUT; think like a rollercoaster line
#operations are enqueue, dequeue, peek/front, isEmpty, size
#FIFO, at least in this case, means no random access
queue_example # more details-->


#   Non-Linear Data Structures
#elements are arranged in a hierarchical or interconnected way
# Trees
#node: data and references to child nodes; fundamental tree building block
#root: topmost node of the tree
#leaf: childless node
#height: length of longest path from the root to any leaf
#depth: length of the path from the root to a specific node
#Binary Tree:
#a binary tree containe at most 2 child elements(left child, right child)
#Binary Search Tree:
#type of binary tree where any nodes child objects follow this rule
#left child < node; right child > node
#Full Binary Tree:
#a binary tree where every node that isnt a leaf has two children
#Complete Binary Tree:
#a binary tree where every node is filled except potentially the last layer(filled left to right)
#Balanced Tree:
#any tree where the height difference between 
#left and right subtrees for any node is no more than 1
#Unbalanced Tree:
#any tree where the height difference between 
#left and right subtrees for any node can be more than 1
tree_example # more details-->


# Graphs
# Graphs are a structure of nodes and edges;trees/linked list are a subset of graphs
#Directed Graph:
#a graph where edges between vertices(nodes) have direction
#edge between node A -> B is different than B -> A
graph_example # more details-->

#Undirected Graph:
#a graph where edges do not have direction
#edge etween node A - B is the same as B - A
graph_example # more details-->

#Spanning Tree:
#subgraph of an undirected graph
#the jist is that a spanning tree is meant to be a methematical simplification
#which avoids any "circuits" <-- loops basically. this reduces the amount of connections
#to the minumum. 
graph_example # more details-->

#Graph Representation
#Adjacency List:
# sorta like {0:[1,3], 1[0], 2[1,3], 3[0,2]}

#Adjacency Matrix:
#matrix chart that shows graph data

# Heaps
heap_example # more details-->

# Hash Table
hashtable_example # more details-->
