### MODULE 2 ###
# If  you want to run any section without any side effects make sure to comment out the other sections
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


# Suppose a == b this means we can set a to any number

# Here i set a to 100
a = 100

# We know a is supposed to be the same as a in value so we can assign the value of b to the value of a
# We could also just assign b to 100: b = 100
b = a

if a - b > 90:
    print('one')
else:
    print('two')
    print('done')

# Next Slide

#Scenario one
original_price = 95
#Scenario two - uncomment other original price values
# original_price = 100
#Scenario three - uncomment other original price values
# original_price = 105

discounted = 0
if original_price > 100:
    discounted = original_price - 20
else:
    discounted = original_price - 10
print(discounted)

def main():
    # We ask for an input and set it to the variable named number
    number = int(input("Enter a number between 1 and 100: "))
    # if the number is greater or equal to one
    if number >= 1:
        # we know the number is greater or equal to one and check if its less then or equal to 100
        if number <= 100:
            print('in range')
        else:
            # The number was greater then 100
            print('too big')
    # we know its less then one
    else:
        print('too small')

# I call the main function which runs the code- try commenting everything else out aside from the code in the main function. Now try running the code
main()



# =============================================================================
#  BEST PRACTICES, TYPE HINTS, REAL-WORLD EXAMPLES
# =============================================================================

print("\n" + "="*50)
print("EXPANDED MODULE 2 CONTENT")
print("="*50)

# Best Practices for Writing Conditionals
print("\n--- BEST PRACTICES FOR CONDITIONALS ---")
# 1. Use clear and descriptive variable names
user_age = 21
has_ticket = True

# 2. Keep conditions simple and readable
if user_age >= 18 and has_ticket:
    print("Entry allowed.")
else:
    print("Entry denied.")

# 3. Avoid deeply nested ifs when possible (use elif or combine conditions)
score = 73
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Grade: {grade}")

# 4. Use comments to clarify complex logic
temperature = 45
# Check for freezing
if temperature <= 32:
    print("Freezing!")
# Check for cold
elif temperature <= 50:
    print("Cold!")
# Otherwise, it's warm or hot
else:
    print("Warm or hot!")

# Type Hints for Conditionals
print("\n--- TYPE HINTS WITH CONDITIONALS ---")
age: int = 17
has_permission: bool = False

if age >= 18 or has_permission:
    print("Access granted.")
else:
    print("Access denied.")

# Real-World Example: Movie Ticket Pricing
print("\n--- REAL-WORLD EXAMPLE: MOVIE TICKET PRICING ---")
customer_age: int = 65
is_student: bool = False
base_price: float = 12.00

if customer_age < 12:
    price = base_price * 0.5  # 50% off for kids
elif customer_age >= 65:
    price = base_price * 0.7  # 30% off for seniors
elif is_student:
    price = base_price * 0.8  # 20% off for students
else:
    price = base_price
print(f"Ticket price: ${price:.2f}")

# Real-World Example: Access Control
print("\n--- REAL-WORLD EXAMPLE: ACCESS CONTROL ---")
username: str = "admin"
password: str = "letmein"

if username == "admin" and password == "letmein":
    print("Access granted!")
else:
    print("Access denied!")

# Challenge: Write a program that checks if a user can rent a car.
# - Must be at least 21 years old and have a valid license (has_license = True)
# - Print 'Rental approved.' or 'Rental denied.'

# Challenge: Write a program that determines the shipping cost:
# - If the order total is $50 or more, shipping is free.
# - If the order total is less than $50, shipping is $5.
# - Use a variable 'order_total'. Print the shipping cost.

# Challenge: Write a program that checks if a year is a leap year using type hints and prints the result.

print("\n" + "="*50)
print("END OF EXPANDED MODULE 2")
print("Great job learning Python conditionals!")
print("="*50)

'''
Summary:
Boolean expressions evaluate to True or False using comparison operators.
Conditional statements (if, else) execute code based on conditions.
Nested if allows more detailed decision-making with multiple levels of conditions.
Multiway conditionals (if, elif, else) let you handle multiple alternative conditions.
Logical operators (and, or, not) help combine multiple conditions.
These concepts are fundamental to making decisions in Python programs.
'''

