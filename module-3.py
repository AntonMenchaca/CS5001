### MODULE 3 ###
# Loops, Iteration, and Control Flow

# FOR LOOPS
print("\n--- FOR LOOPS ---")
# Loop over a range of numbers
for i in range(5):
    print(f"i is {i}")

# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Loop over a string
word = "hello"
for letter in word:
    print(letter)

# Challenge: Print all numbers from 1 to 10 using a for loop.


# WHILE LOOPS
print("\n--- WHILE LOOPS ---")
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# Challenge: Use a while loop to print numbers from 10 down to 1.


# RANGE FUNCTION
print("\n--- RANGE FUNCTION ---")
for num in range(2, 11, 2):
    print(f"Even number: {num}")

# Challenge: Use range to print all odd numbers from 1 to 19.


# BREAK AND CONTINUE
print("\n--- BREAK AND CONTINUE ---")
for n in range(1, 10):
    if n == 5:
        print("Breaking at 5!")
        break
    if n % 2 == 0:
        print(f"Skipping even number: {n}")
        continue
    print(f"Number: {n}")

# Challenge: Use break to stop a loop when a number is divisible by 7.


# LOOPING OVER STRINGS AND LISTS
print("\n--- LOOPING OVER STRINGS AND LISTS ---")
name = "Python"
for char in name:
    print(char.upper())

numbers = [3, 7, 2, 9]
sum_numbers = 0
for number in numbers:
    sum_numbers += number
print(f"Sum of numbers: {sum_numbers}")

# Challenge: Loop through a list of names and print a greeting for each.


# NESTED LOOPS
print("\n--- NESTED LOOPS ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# Challenge: Print a multiplication table (1-5) using nested loops.


# COMMON LOOP PITFALLS
print("\n--- COMMON LOOP PITFALLS ---")
# Infinite loop example (don't run this!):
# while True:
#     print("This will run forever!")

# Off-by-one error example:
for i in range(5):  # Prints 0 to 4, not 0 to 5
    print(i)

# Challenge: Fix the off-by-one error to print 1 to 5.


# REAL-WORLD EXAMPLE: SUMMING USER INPUTS
print("\n--- REAL-WORLD EXAMPLE: SUMMING USER INPUTS ---")
total = 0
for _ in range(3):
    # num = int(input("Enter a number: "))
    num = 5  # Simulated input
    total += num
print(f"Total sum: {total}")

# Challenge: Write a program that asks the user for 5 numbers and prints their average.


# SUMMARY
print("\n--- SUMMARY ---")
print("- For loops: iterate over sequences or ranges")
print("- While loops: repeat until a condition is false")
print("- Use break/continue to control loop flow")
print("- Use range() for number sequences")
print("- Avoid infinite loops and off-by-one errors!")
print("- Practice makes perfect!")
