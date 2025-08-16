### MODULE 4 ###
# Functions, Parameters, Return Values, and Scope

# DEFINING AND CALLING FUNCTIONS
print("\n--- DEFINING AND CALLING FUNCTIONS ---")
def greet():
    print("Hello!")

greet()

# Challenge: Write a function that prints your name.


# PARAMETERS AND ARGUMENTS
print("\n--- PARAMETERS AND ARGUMENTS ---")
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

greet_person("Bob")

# Challenge: Write a function that takes two numbers and prints their sum.


# RETURN VALUES
print("\n--- RETURN VALUES ---")
def add(a, b):
    return a + b

result = add(3, 4)
print(f"3 + 4 = {result}")

# Challenge: Write a function that returns the square of a number.


# SCOPE (LOCAL VS GLOBAL VARIABLES)
print("\n--- SCOPE (LOCAL VS GLOBAL VARIABLES) ---")
x = 10

def print_x():
    x = 5  # Local variable
    print(f"Inside function, x = {x}")

print_x()
print(f"Outside function, x = {x}")

# Challenge: Write a function that modifies a global variable.


# DEFAULT PARAMETERS
print("\n--- DEFAULT PARAMETERS ---")
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9
print(power(3, 3))   # 27

# Challenge: Write a function with a default parameter for a greeting message.


# KEYWORD ARGUMENTS
print("\n--- KEYWORD ARGUMENTS ---")
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(name="Whiskers", animal="cat")

describe_pet("dog", "Buddy")

# Challenge: Call a function using keyword arguments in a different order.


# RETURNING MULTIPLE VALUES
print("\n--- RETURNING MULTIPLE VALUES ---")
def min_max(numbers):
    return min(numbers), max(numbers)

nums = [3, 7, 2, 9]
minimum, maximum = min_max(nums)
print(f"Min: {minimum}, Max: {maximum}")

# Challenge: Write a function that returns both the sum and average of a list.


# REAL-WORLD EXAMPLE: TEMPERATURE CONVERTER
print("\n--- REAL-WORLD EXAMPLE: TEMPERATURE CONVERTER ---")
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}F = {temp_c:.2f}C")

# Challenge: Write a function that converts Celsius to Fahrenheit.


# SUMMARY
print("\n--- SUMMARY ---")
print("- Functions group code for reuse and clarity")
print("- Use parameters to pass data in, return to send data out")
print("- Scope controls where variables exist")
print("- Default and keyword arguments add flexibility")
print("- Practice writing and calling functions!")
