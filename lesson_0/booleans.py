# Definition: A "boolean" is a value of either True or False
#
# We can assign booleans to variables just like we can numbers
#   x = True
#   y = False
#
# We can also compare booleans using boolean operators
#
#  not  -> flips the value of the boolean (in other languages written as '!')
#  and  -> returns True if and only if both values are True (in other languages written as '&&')
#  or   -> returns True if at least one of the values is True (in other languages written as '||')
#   ^   -> "exclusive or" or "nor" returns True if and only if exactly one of the values is True
#
# Try and answer the following boolean comparisons, then test your work in the
# python interpreter on your terminal
#
    1) True and False                =
    2) False or True                 =
    3) not True or False             =
    4) True and not False            =
    5) not False and True or False   =
    6) False or False and True       =
    8) False or True ^ True or False =

# While not, and, or, ^ operate on booleans alone, there are two more operators
# that we can use to get boolean results from comparing non-boolean values
#
# x == y  -> resolves to True iff both x and y are equivalent       -> e.g. 1 == 3 is False
# x != y  -> resolves to True iff both x and y are not equivalent   -> e.g. 1 != 3 is True
#
# With the use of these operators, we gain the ability to introduce new control structures
# that we can use to write more complex tasks


# This function exemplifies how to use if/else statements
def isTrue(b: bool):
    if b:
        print("This is true")
    else:
        print("This is false")

# This function exemplifies how to use a while statement
def countDown(x: int):
    while x >= 0:
        print(x)
        x -= 1

# Let's try some practice problems using if and while statements
#
# if statements

# print out whether the number x is positive, negative, or zero
def sign(x: int):

# print out if x is greater than, less than, or equal to zero
def relation(x: int, y: int):

# return x to the power of y
def exponentiate(x: int, y: int) -> int:

# return True if the number is odd, even otherwise
def isOdd(x: int) -> bool:

# write out the digits of x
def writeDigits(x: int):
    
