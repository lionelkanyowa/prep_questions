# 1. Concatenate two strings, one with your first name and one with your last, to create a new string 
# with your full name as its value. For example, if your name is John Doe, you should combine 
# 'John' and 'Doe' to get 'John Doe'.

fname = 'Lionel'
lname = 'Kanyowa'

print(fname + ' ' + lname)

# ==================================================================================

# 2.This question may be a little challenging if your math skills are rusty. Don't be afraid to 
# take advantage of the hints. Try your best to solve the problem, but don't feel 
# compelled to complete it if you become frustrated.

# ==================================================================================

# 3. What does the following code do and why?
print('5' + '10')

# It outputs the value '510. When two string values are added using the addition operator, they
# are combined instead of being added together therefore final output would be '510'


# ==================================================================================

# 4. Refactor the code from the previous exercise to use coercion to print 15 instead.
# print('5' + '10')

print(5 + 10)

# ==================================================================================

# 5. Will an error occur if you try to access a list element with an index greater than or equal to the list's length? For example:
foo = ['a', 'b', 'c']
print(foo[3]) # Wil this result in an error?
# This will result in an error, an IndexError to be exact because there is no value on the third index of the list.

# ================================================================================== 

# 6.To what value does the following expression evaluate?
'foo' == 'Foo'
# Evaluates to false as case sensitivity matters when comparing strings

# ================================================================================== 

# 7.What will the following code do? Why?
int('3.1415')
# It raises a ValueError since the string value '3.1415' is not a valid number/integer.

# ================================================================================== 

# 8.To what value does the following expression evaluate?

'12' < '9'

# This expression would evaluate to True since the string values are compared character by character from left to right.
# First we compare 1 and 9, and since 1 is less than 9, the evaluation stops and returns True.



