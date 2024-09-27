import builtinfunctions
import customfunctions

#CONTROL FLOW

#   if else Statements
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

#   for Statements
words = ['imagine', 'dragons', 'yellow']
for w in words:
    print(w, len(w))
#   The range Function
for i in range(5):
    print(i)

#   break and continue Statements
#break statement breaks out of innermost for or while loop
break

#   pass Statements
#a pass statement does nothing. It is used when a statement is required syntactically, 
#but not action is otherwise required.

#   match Statements
#match statement takes an expression and compares its value to many "cases"
def dayRepeater(day):
    match day:
        case Monday:
            return "Ugh I hate mondays lol - garfield"
        case Tuesday:
            return "2's day!"
        case Wednesday:
            return "Hump day!"
        case _:
            return "I don't know that day lol"

#   Functions
customfunctions # more details-->

#   Built-In Functions
builtinfunctions # more details-->
