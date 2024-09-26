import bitwiseoperators
#BUILT-IN OPERATORS

#   Arithmetic Operators
a + b # Addition
a - b # Subtraction
a * b # Multiplication
a / b # Division
a // b # Floor Division
a % b # Modulus(Remainder)
a ** b # Eaponentiation

#   Comparision/Relational Operators
a == b # Equal to
a != b # Not Equal to
a > b # Greater Than
a < b # Less Than
a >= b # Greater Than or Equal to
a <= b # Less than or Equal to

#   Logical Operator
(a > b) and (c < d) # True if both operands are true
(a > b) or (c < d) # True if at least one operand is true
not (a > b) # Inverts the boolean value

#   Bitwise Operators
#bitwise operators are used to perform operations directly on the "binary representations"
#of integers. since they manipulate individual bits of data, they are used in low-level
#programming tasks. (optimization, performance enhancement, working with hardware/network protocols)
a & b # Bitwise AND
a | b # Bitwise OR
a ^ b # Bitwise XOR
~a # Bitwise NOT
a << 2 # Left Shift
a >> 2 # Right Shift
bitwiseoperators # more details-->


#   Assignment Operator
a = 5 # Assign
a += 5 # Add and Assign
a -= 5 # Subtract and Assign
a *= 5 # Multiply and Assign
a /= 5 # Divide and Assign
a //= 5 # Floor Divide and Assign
a %= 5 # Modulus and Assign
a **= 5 # Eaponentiate and Assign
a &= 5 # Bitwise AND and Assign
a |= 5 # Bitwise OR and Assign
a ^= 5 # Bitwise XOR and Assign
a <<= 5 # Left shift and Assign
a >>= 5 # Right shift and Assign

#   Identity Operators
a is b # is
a is not b # is not

#   Membership Operator
a in b # in
a not in b # not in

#   Ternary(Conditional) Operators
# similar to if else statements but slightly different
# conditional operators are good for simple cases and if elese statements for more complex
status = "Adult" if age >= 18 else "Minor" # value_if_true if condition else value_if_false

#OPERATOR PRECEDENCE