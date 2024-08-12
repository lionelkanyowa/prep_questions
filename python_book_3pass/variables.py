# 1.Classify the following potential non-constant variable names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.

# Name           | variable         | Reason
# index          | idiomatic        | All lowercase
# CatName        | non-idiomatic    | Starts with capital letters for each word
# lazy_dog       | idiomatic        | Uses snake_case
# quick_Fox      | non_idiomatic    | Has a capital letter
# 1stCharacter   | illegal          | Starts with a number
# operand2       | idiomatic        | contains lowercase and a digit
# BIG_NUMBER     | non-idiomatic    | Contains uppercase letters
# π              | idiomatic        | Not part of the ASCII character set


# =======================================================================================

# 2.Classify the following potential function names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic 
# and illegal names, explain your choice.

# Name           | variable         | Reason
# index          | idiomatic        | All lowercase
# CatName        | non-idiomatic    | Starts with capital letters for each word
# lazy_dog       | idiomatic        | Uses snake_case
# quick_Fox      | non-idiomatic    | Contains a capital letter
# 1stCharacter   | illegal          | Starts with a number
# operand2       | idiomatic        | Contains lowercase and a digit
# BIG_NUMBER     | non-idiomatic    | SCREAMING SNAKE_CASE
# π              | idiomatic        | Not part of the ASCII character set

# =======================================================================================

# 3.Classify the following potential constant names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.

# Name           | variable         | Reason
# index          | non_idiomatic    | All lowercase
# CatName        | non-idiomatic    | Starts with capital letters for each word only 
# snake_case     | non-idiomatic    | Uses snake_case
# lAZY_DOG3      | idiomatic        | SCREAMING_SNAKE_CASE
# 1ST            | illegal          | Starts with a number
# operand2       | non-idiomatic    | lowercase and a digit 
# BIG_NUMBER     | idiomatic        | SCREAMING_SNAKE_CASE 
# π              | non-idiomatic    | Not part of the ASCII character set 

# =======================================================================================

# 4. Classify the following potential class names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.

# Name           | variable         | Reason
# index          | non_idiomatic    | All lowercase
# CatName        | idiomatic        | Uses CamelCase
# Lazy_Dog       | non_idiomatic    | Should not contains snake_case
# 1ST            | illegal          | Starts with a number
# operand2       | non-idiomatic    | lowercase and a digit 
# BigNumber3     | idiomatic        | Uses CamelCase
# Πi             | non-idiomatic    | Not part of the ASCII character set 

# =======================================================================================

# 5. Write a program named greeter.py that greets 'Victor' three times. Your program should 
# use a variable and not hard code the string value 'Victor' in each greeting. Here's an example run of the program:

# $ python greeter.py
# Good Morning, Victor.
# Good Afternoon, Victor.
# Good Evening, Victor.

name = 'Victor'
print(f'Good Morning {name}.')
print(f'Good Afternoon {name}.')
print(f'Good Evening {name}.')

# =======================================================================================

# 6. Write a program named age.py that includes someone's age and then calculates and reports the future age 10, 20, 30, 
# and 40 years from now. Here's the output for someone who is 22 years old.

# You are 22 years old.
# In 10 years, you will be 32 years old.
# In 20 years, you will be 42 years old.
# In 30 years, you will be 52 years old.
# In 40 years, you will be 62 years old.

age = 36
print(f'You are {age} old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')

# =======================================================================================

# 7.What happens when you run the following code? Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# It outputs the following:

# Good Morning Victor.
# Good Afternoon Victor.
# Good Evening Victor.

# Good Morning Nina.
# Good Afternoon Nina.
# Good Evening Nina.

# Although name is a constant, Python doesn't know that it is a constant, therefore the constant variable
# was originally assigned to the string 'Victor' has been reassigned to the string 'Nina'.
# It is up to the programer to keep a track of the constant variable.

# =======================================================================================

# 8.Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% 
# (this is a wish-fulfillment fantasy) compounded interest every year. After one year, you will have $1,050 ($1,000 times 1.05). 
# After two years, you will have $1,050 times 1.05, or $1102.50. Create a variable named balance that contains the amount 
# of money you will have after 5 years, then print the result. Use a single expression if you can to set balance to the correct value. 

balance = (1000 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05)
print(balance) 


# =======================================================================================
# 9.Repeat the previous question but, this time, use augmented assignment to compute the final result, 
# one year at a time.
balance = 1000
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
print(balance)

# =======================================================================================

# 10.  Assume that obj already has a value of 42 when the code below starts running. 
# Which of the subsequent statements reassign the variable? Which statements mutate the 
# value of the object that obj references? Which statements do neither? If necessary, 
# you can read the documentation.

obj = 'ABcd'        # Reassigns variable 
obj.upper()         # neither
obj = obj.lower()   # Reassigns variable
print(len(obj))     # neither
obj = list(obj)     # Reassigns variable
obj.pop()           # Mutates variable
obj[2] = 'X'        # Mutates variable
obj.sort()          # Mutates variable
set(obj)            # nether
obj = tuple(obj)    # Reassigns variable
