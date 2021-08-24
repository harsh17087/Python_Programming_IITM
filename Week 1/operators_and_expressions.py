# We'll look into some operators and expressions

a = "Programming in"
b = "Python"
print("We can concatenate two strings by addition operator i.e.", a, "+", b, "after concatenation yields", a + b)

# Python follows precedence i.e. a rule to evaluate expressions for example

sum = 2 + 5 * 6 / 8
print(sum)
# the output is 5.75

'''
The precedence order is shown below in decreasing priority

                ()                                    	Parentheses
                **	                                    Exponent
                +x, -x, ~x	                            Unary plus, Unary minus, Bitwise NOT
                *, /, //, %	                            Multiplication, Division, Floor division, Modulus
                +, -	                                Addition, Subtraction
                <<, >>	                                Bitwise shift operators
                &	                                    Bitwise AND
                ^	                                    Bitwise XOR
                |	                                    Bitwise OR
==, !=, >, >=, <, <=, is, is not, in, not in	        Comparisons, Identity, Membership operators
             not	Logical NOT
             and	Logical AND
              or	Logical OR
'''

# Let's see some more arithmetic operators

print("exponential i.e. 2^5 is", 2 ** 5)
print("floor division i.e. 5//2 yields", 5 // 2)
print("Modulo means remainder i.e. 9%7 is", 9 % 7)
print("5 > 2 yields boolean value i.e. either true or false. In this case it's", 5 > 2)
print("True and True yields", True and True)
print("False and True yields", False and True)

# The output of the above programs are shown below
'''
exponential i.e. 2^5 is 32
floor division i.e. 5//2 yields 2
Modulo means remainder i.e. 9%7 is 2
5 > 2 yields boolean value i.e. either true or false. In this case it's True
True and True yields True
False and True yields False

'''
