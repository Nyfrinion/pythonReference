import builtinexceptions
#EXCEPTION HANDLING

#   try, except, else, finally Block Structure
try:
# Code that might raise an exception
    risky_operation()
except SomeException:
# Multiple exception blocks can be used 
# in order to catch different types of exceptions
# Code to handle the exception
    handle_error()
else:
# Code to run if no exception occurs
    execute_if_no_exception()
finally:
# Code that will run no matter what
    cleanup_code()
#the else and finally blocks are optional

#   Catch-all Exception
# it is possible to catch all exceptions, but is not recommended
# this is because it may hide the nature of the error
try:
    risky_operation()
except Exception as e:  # Captures any exception
    print(f"An error occurred: {e}")

#   Raising Exceptions
#exceptions can be raised manually in order to enforce certain conditions.
def check_positive(n):
    if n < 0:
        raise ValueError("Negative number not allowed.")
    return n

#   Custom Exceptions
#custom exceptions are created via "subclassing" pythons exception class
class MyCustomError(Exception):
    pass

#   Built-In Exceptions
builtinexceptions # more details--> 
