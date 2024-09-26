import types
import operators
import objectoriented
import controlflow
import exceptionhandling
import lambdafunctions
import filehandling
import decorators
import generators
import contextmanagers

#COMMENTS
#hashtags are used for comments
#use CTRL + / for comment and uncomment.. 

#INDENTATION
#python uses indentation instead of brackets
if x > 10:
    print("the value is greater than 10")

#VARIABLES
#variables are "dynamically" typed rather than "strongly" typed
#this means that the data type is inferred from the value rather than explicity stated
#ex: int a = 10 vs a = 10; in the latter case python simply recognizes that 10 is an integer
types # more details--> 

#OPERATORS
#operators allow you to complete certain types of actions between variables/datatypes
#like mathematic operators(+, -, etc)
operators # more details--> 

#CONTROL FLOW
#python has many different ways of controlling the code flow
#   Statements: Instruction that the python interpreter can execute; does not return a value
print("Hey, Look, Listen!") 

#   Expression: Combination values, variables, operators and function calls; returns a value
x > 5 #returns true or false

#   Loops: Control flow statements that repeat
for i in range(5):
    print(i)

#   Functions: a reusable block of code; can take inputs(arguements) and return an output value
def add(a, b):
    return a + b
controlflow # more details--> 

#CLASSES
#   Class: a blueprint for creating "objects". It defines a set of attributes and methods
#   any object from this class will have these.
class Dog:
    species = "Canis familiaris" # class attribute -> shared amongst all instances of the class
    def __init__(self, name, breed):
        self.name = name  # instance attribute -> specific to instance/object
        self.breed = breed  # instance attribute

    def bark(self):  # instance method -> defined to operate on an instance
        return "Woof!"

    @classmethod
    def get_species(cls):  # class method -> can access class attributes
        return cls.species

    @staticmethod
    def info():  # static method -> these do not access class/instance attributes; act like regular functions but are associated with the classe
        return "Dogs are loyal animals."

#   Object: any instance of a class. It has encapsulated properties(attributes) and behaviors(methods);
#   methods are functions in a class context and typically have access to class or instance attributes
my_dog = Dog("Ridge", "Greate Pyrenees")
objectoriented # more details--> 

#EXCEPTION HANDLING
#exception handling is a process designed for managing errors
#   Errors: Issues that arise during program execution; often halt execution
#   syntax errors show up before running; runtime errors often reflect illegal operations
#   that occur once the program runs
#   Exceptions: Exceptions are events that disrupt the normal flow of your program
#   they are "raised" when specific conditions are met and can be caught and handled
#   python has built in exception types and allows for custom ones
exceptionhandling # more details--> 

#MODULES AND IMPORTS
#   Module: a file containing python code that can be used by other python programs.abs
#   for a module to be used it must be imported
import modules
print(module.fake_function())
#   additionally, you can import specific functions or classes
from modules import fake_function, fake_class
print(fake_function())
#   finally, you can import all functions or classes
#   this is not recommended due to potentially naming conflicts with one of the imported functions/classes
from modules import *
print(fake_function())
#   you can "alias" a module and change its name upon import
import modules as m
print(m.fake_function())

#   Packages: a collection of (usually related) modules
#   packages contain their modules and a __init__.py file. This file can be empty
from package import module_a, module_b, module_c

#LIST COMPREHENSTIONS
#an effecient/compact way of creating lists based on existing lists
types # more details--> 

#LAMBDA FUNCTIONS
#   Lambda Function: small, single-line, "anonymous" function 
#   that is not intended for reuse anywhere else in the code
#   anonymous means it has no name
lambdafunctions # more details--> 

#FILE HANDLING
#file handling includes creating, reading, writing and manipulating system files
filehandling # more details--> 

#DECORATORS
#functions that modify the behavior of another function
decorators # more details-->

#GENERATORS
#functions that yield values one at a time using yield
generators # more details-->

#CONTEXT MANAGER
#???
contextmanagers # more details-->







