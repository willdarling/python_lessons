# The last primitive data type in Python that we need to learn is called a string
# which we've actually seen before back in our first function, reproduced below

def helloWorld():
    print("Hello world")

# In this function, the argument "Hello world" to the function print() is an
# example of a string
#
# Definition: a string is a collection of alphanumeric characters and symbols
# in double or single quotes
#
# Try printing out some examples of strings in the terminal. Remember, while most
# strings will consist primarily of letters, we can still get numbers and symbols.
# For example, '1+1' is a string!
#
# Operations on strings:
#
# We can compare strings to see if they're the same word using '==' and '!='
# e.g. 'hello' != 'world' -> True
#      'hello' == 'hello' -> True
#
# And append two strings together using '+'
# e.g. 'hello' + 'world' -> 'helloworld'
#
# We can also find the length of a string using the len() function
# e.g. len("hello world ") -> 11
#
# Finally, we can reference any given letter of a string by adding square brackets
# to the end of the variable name, and specifying an index inside those brackets
# from 0 to len(s)-1, where 0 is the first letter.
#
# s = "hello"
# print(s[0]) -> 'h'
#
# And when looking at individual characters, we can use >, >=, <, <= to check
# the alphabetic order of individual characters. If a letter is earlier in the
# alphabet, it is considered less than
# e.g. a < b -> True
#
# Let's write some functions to get used to using these tools

# Given two strings s1 and s2 return the longer string
def longestWord(s1: string, s2: str) -> str:

# Given two strings s1 and s2 return the string who's first letter comes earliest
# in the alphabet. If both strings start with the same letter, return s1
def alphabetizeSimple(s1: str, s2: str) -> str:

# Given two strings s1 and s2 return the string that comes earliest in the alphabet.
# If the strings are equivalent, return either string.
def alphabetize(s1: str, s2: str) -> str:
