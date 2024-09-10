### MODULE 2 ###

'''
Comparison Operators:
== : Equals
!= : Not equals
< : Less than
> : Greater than
<= : Less than or equal to
>= : Greater than or equal to
'''

# Boolean Expression Example
a = 5
b = 10

print(a > b)   # Output: False (since 5 is not greater than 10)
print(a == 5)  # Output: True (since a is equal to 5)

# Challenge: Compare two numbers using boolean expressions and print the results.


'''
Conditional statements allow you to execute certain blocks of code based on whether a condition is true or false. 
The most common conditional statement is the if statement.
'''

# Conditional Statement Example
age = 18

if age >= 18:
    print("You are an adult.")  # This will print if the condition is True
else:
    print("You are a minor.")   # This will print if the condition is False

# Challenge: Check if a number is positive, negative, or zero using conditional statements.

'''
A nested if statement is when one if statement is placed inside another if statement. 
This allows you to check for more complex conditions.
'''

# Nested if Example
grade = 85

if grade >= 60:
    if grade >= 90:
        print("You got an A!")
    else:
        print("You passed!")
else:
    print("You failed!")

# Challenge: Create a nested if statement that checks the age and license status.


'''
A multiway conditional uses if, elif, and else to handle multiple conditions. 
The elif (short for "else if") allows for checking multiple conditions sequentially.
'''

# Multiway Conditionals Example
temperature = 75

if temperature > 90:
    print("It's hot outside.")
elif temperature > 60:
    print("It's warm outside.")
else:
    print("It's cold outside.")

# Challenge: Use multiway conditionals to determine a letter grade based on a number.


'''
Logical operators are used to combine multiple Boolean expressions. In Python, we use the following:

and: Both conditions must be true.
or: At least one condition must be true.
not: Inverts the truth value
'''

# Logical Operators Example
age = 20
has_license = True

# Check if the person is old enough to drive and has a license
if age >= 18 and has_license:
    print("You can drive!")
else:
    print("You cannot drive yet.")

# Check if the person is not a minor
if not age < 18:
    print("You are not a minor.")


# Challenge: Use logical operators to check both the age and license status.

'''
Summary:
Boolean expressions evaluate to True or False using comparison operators.
Conditional statements (if, else) execute code based on conditions.
Nested if allows more detailed decision-making with multiple levels of conditions.
Multiway conditionals (if, elif, else) let you handle multiple alternative conditions.
Logical operators (and, or, not) help combine multiple conditions.
These concepts are fundamental to making decisions in Python programs.
'''

