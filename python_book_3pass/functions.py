# 1 What happens when you run the following program? Why do we get that result?

#def set_foo():
    #foo = 'bar'

#set_foo()
#print(foo)

# We are getting a NameError, with the reason that "name'foo' is not defined". In line 4, the variable foo is assigned to the string
# 'bar', however, there is no variable outside of the function, therefore when printing foo we get an error because anything inside
# the function cannot be accessed from the outside since it's not in scope.

# ================================================================================================

# 2.Take a look at this code snippet:

#foo = 'bar'

#def set_foo():
    #foo = 'qux'
    
#set_foo()
#print(foo)

# What does this program print? Why?
# This prints the string 'bar'. The variable 'foo' outside of the function is the one being printed
# in line 23. 

# ================================================================================================

# 3.Write a program that uses a multiply function to multiply two numbers and returns the result. 
# Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

# $ python multiply.py
# Enter the first number: 3.1416
# Enter the second number: 2.7183
# 3.1416 * 2.7183 = 8.53981128

#def multiply_numbers(x, y):
    #return x * y

#num1 = float(input('Enter the first number: '))
#num2 = float(input('Enter the second number: '))

#sum = multiply_numbers(num1, num2)
#print(f'{num1} * {num2} = {sum}')


# ================================================================================================

# 4. Consider this code:
#def multiply_numbers(num1, num2, num3):
    #result = num1 * num2 * num3
    #return result

#product = multiply_numbers(2, 3, 4)

# Identify the following items in that code:

# Item                      |
# function name             | line 52, 56 (multiply_numbers)
# function arguments        | line 56 (2, 3, 4) 
# function definition       | line 52-54 (Everything)
# function body             | line 53, 54 (Everything)
# function parameters       | line 52 (num1, num2, num3)
# function invocation       | line 56 (multiply_numbers(2, 3, 4))
# function return value     | line 54
# all identifiers           | line multiply_numbers, num1, num2, num3, result, product

# ================================================================================================
# 5.What does the following code print?
#def scream(words):
    #return words + '!!!!'

#scream('Yipeee')

# There is no output. The function returns the value 'Yipeee'. But nothing is done,
# since the print() function is never called. 

# ================================================================================================

# 6. What does the following code print? 

#def scream(words):
    #words = words + '!!!!'
    #return
    #print(words)
    
#scream('Yipeee')

# There is not output. The return on line 86 terminates the function before the function moves to 
# print(words)

# ================================================================================================

# 7. Without running the following code, what do you think it will do?
#def foo(bar, qux):
   #print(bar)
    #print(qux)
    
#foo('Hello')

# This will output an error (TypeError). The function definition has 2 parameter to pass through 2 arguments.
# Only one argument is passed in line 101. 

# ================================================================================================

# 8. Without running the following code, what do you think it will do?

#def foo(bar, qux):
    #print(bar)
    #print(qux)
    
#foo(42, 3.141592, 2.718)

# This will output an error (TypeError). The function definition has 2 parameters to pass through 2 arguments.
# 3 arguments are passed in line 114. 

# ================================================================================================
# 9. Without running the following code, what do you think it will do?

#def foo(first, second =3, third=2):
    #print(first)
    #print(second)
    #print(third)

#foo(42, 3.141592, 2.718)

# The code will output 42, 3.141592, 2.718. Since foo has three parameters, the second and third have default values.
# We passed the function three arguments, Python ignores the default values.

# ================================================================================================

# 10. Without running the following code, what do you think it will do?

#def foo(first, second=3, third=2):
    #print(first)
    #print(second)
    #print(third)

#foo(42, 3.141592)

# The code will output 42, 3.141592, 2. Since foo has three parameters, the second and third have default values.
# We passed the function three arguments, Python uses the default value for the last argument.

# ================================================================================================

# 11.Without running the following code, what do you think it will do?

#def foo(first, second=3, third=2):
    #print(first)
    #print(second)
    #print(third)
    
#foo(42)

# The code will output 42, 3, 2. Since foo has three parameters, the second and third have default values.
# We passed the function with one argument, Python uses the default value for the last two argument.

# ================================================================================================

# 12. Without running the following code, what do you think it will do?

#def foo(first, second=3, third=2):
    #print(first)
    #print(second)
    #print(third)
    
#foo()
# Nothing will be printed. There will be a TypeError. since no arguments were passed within the calling function and the 
# first parameter has no default value.

# ================================================================================================

# 13. Without running the following code, what do you think it will do?

#def foo(first, second=3, third):
    #print(first)
    #print(second)
    #print(third)
    
#foo(42)

# This will output a SyntaxError. Although we have an argument passed for the first parameter and a default value
# for the second argument, we have neither for the third argument. 

# ================================================================================================

# 14.Identify all of the identifiers on each line of the following code.
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')
