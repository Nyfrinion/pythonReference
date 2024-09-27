import iterables
#BUILT-IN FUNCTIONS
#note: for more details check python documentation.

#   Input/Output
input()
print()
open()

#   Type Conversion
bool()
bin(int) # binary string: convert an integer to a binary string prefixed with "0b"
bytearray() #byte array: return a new array of bytes; byte array class is a mutable
#sequence of integers from 0 to 256.
bytes() # bytes: returns a new bytes object which is a immutable sequence of integers 
#from 0 to 256
complex()
dict()
float()
frozenset()
int()
list()
set()
str()
tuple()
format()

#   Mathematical Operations
abs() # absolute value: returns the absolute value/magnitude of 
#(int, float, complex number)
pow()
round()
divmod()
bin()
hex()
oct()

#   Data Handling
lens()
max()
min()
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
