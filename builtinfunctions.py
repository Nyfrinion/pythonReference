import iterables
#BUILT-IN FUNCTIONS
#note: for more details check python documentation.

#   Input/Output
input()
print()
open()

#   Type Conversion
bool() # bool: returns a true or false 
bin(int) # binary string: convert an integer to a binary string prefixed with "0b"
bytearray() #byte array: return a new array of bytes; byte array class is a mutable
#sequence of integers from 0 to 256.
bytes() # bytes: returns a new bytes object which is a immutable sequence of integers 
#from 0 to 256
complex() #complex: just creates a complex literal?
dict() # dictionary: creates a dictionary
float() # float: converts to float
frozenset() # frozenset: creates a frozenset
int() # int: converts to int
list() # list: converts to list
set() # set: creates a set
str()
tuple() # tuple: converts to tuple
format()

#   Mathematical Operations
abs() # absolute value: returns the absolute value/magnitude of 
#(int, float, complex number)
pow() # power: exponent operator with an optional modulus arguement (a ** b) % c ?
#much more effecient if your exponent is large
round() # round: used to round numbers to a decimal given in the argument. 
#floating point error may return unexpected rounding results
divmod() # div mod: accepts arguements for quotient and remainder??
bin()
hex()
oct()
sum() # sum: sums up iterables; customizable? 



#   Data Handling
lens()
max() # max: return largest number of argument(s)
min() # min: return smallest number of argument(s)
sum()
sorted()
reversed()
enumerate()
zip()

#   Object Introspection
type()
id()
isinstance()
issubclass()
dir()
vars()
getattr()
setattr()
hasattr()
delattr()

#   Iterators/Iteratables
aiter(async_iterable) #async interator: returns an asynchronous iterator 
#for an ansynchronous iterable
iter()
next()
await anext(async_iterable, default) #async next: default is optional. 
#return the next item from the given asynchronus iterable when awaited. 
#or default if the given and the iterator is exhausted
map()
filter()
range()
all(iterable) # all: return true if all elements of the 
#iterable are true(or iterable is empty)
any(iterable) #any: return true is any element of the
#iterable is true. If iterable is empty, return false
iterables # more details-->
awaitables # more details-->

#   Functional Programming
classmethod()
staticmethod()
property()

#   Miscellaneous
help()
eval()
exec()
compile()
chr()
globals()
local()
callable() # returns true of arguement appears callable; false if not
ascii()
repr()
hash()
breakpoint(*args, **kws) # drops you into the debugger at the call site
#the arguments are flexible here and allow you to pass in important information
#for errors
