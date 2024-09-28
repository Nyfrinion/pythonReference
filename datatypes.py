import iterables
#BUILT IN TYPES
#primitives -> int, string, char, float, etc
#composite -> list, dict, tuple, set, etc
datastructures # more details-->



#   Mutability
#mutability reflects a types ability to change its state or value after its creation
#ex: strings are immutable; 
#operations that appear to change the string actually create a new one
#therefore mutable object can stand to be quicker and more memory friendly
#when considering concurrency however, immutable objects are preferable/more secure
#this avoids a case where multiple threads attempt to modify the same mutable object simultaneously

#   Numeric Types
x = 5 # int; immutable
x = 5.25 # float; immutable
x = 5 + 3j # complex; immutable

#   Sequence Types
x = "string" # str; immutable
x = ["element_1","element_2","element_3"] # list; mutable
x = ("value_1","value_2") # tuple; immutable
range(5) # range; range(start,stop,step)

#   String Interpolation

#   Mapping Type
x = {"name": "Alice", "age": 30} # dict; mutable
# dictionary type is a collection of "key-value pairs". They allow for quick lookups.

#   Set Types
x = {1,2,3,3} # set; mutable
#sets are an unordered collection of unique items; multiple values are ignored
x = frozenset([1,2,3,3]) # frozenset; immutable
#set which cannot be changed

#   Boolean Type
x = false # bool; immutable

#   Binary Types
x = 5 # byte; immutable
x = 5 # bytearray; mutable
x = 5 # memoryview; 

#   None Type
x = None # none

#   Callable Types
#callable types are methods, functions, etc

#   Iterator and Generator Types
#iterator and generator types are used to iterate over a collection of items
#they are used to traverse data structures

#   Iterator
#iterator implements the "iterator protocol"
#they are "stateful" meaning they maintain their state; aka current position of the iteration
#they are "single-pass" meaning they can only traverse the data structure once
#afterwards a new iterator will need to be created
iter()
next()
#   Custom Interator
__iter__
__next__
#   Generator
iterables # more details-->

#   Context Manager Types
x = 5 # int

#   Type Hints

#   Type Casting
#converting one datatype to another
#   Implicit: automatic conversion
new_number = integer_number + float_number  # integer_number is automatically converted to a float
#   Explicit: manual conversion
num_string = int(num_string)