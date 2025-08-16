### MODULE 5 ###
# Lists, Indexing, Slicing, and List Methods

# LIST BASICS
print("\n--- LIST BASICS ---")
numbers = [10, 20, 30, 40, 50]
print(numbers)

# Accessing elements by index
print(numbers[0])  # First element
print(numbers[-1]) # Last element

# Challenge: Print the second and fourth elements of the list.


# SLICING LISTS
print("\n--- SLICING LISTS ---")
print(numbers[1:4])   # Elements at index 1, 2, 3
print(numbers[:3])    # First three elements
print(numbers[2:])    # From index 2 to end

# Challenge: Print every other element in the list using slicing.


# LIST METHODS
print("\n--- LIST METHODS ---")
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.insert(1, "blueberry")
print(fruits)

# Challenge: Add an item to a list, then remove a different item.


# LOOPING OVER LISTS
print("\n--- LOOPING OVER LISTS ---")
for num in numbers:
    print(num)

for i in range(len(fruits)):
    print(f"Fruit {i}: {fruits[i]}")

# Challenge: Print all elements of a list in reverse order.


# LIST COMPREHENSIONS
print("\n--- LIST COMPREHENSIONS ---")
squares = [x ** 2 for x in range(1, 6)]
print(squares)

# Challenge: Create a list of even numbers from 2 to 20 using a list comprehension.


# NESTED LISTS
print("\n--- NESTED LISTS ---")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # 6

# Challenge: Print all elements in a 2D list (matrix) row by row.


# REAL-WORLD EXAMPLE: GRADES
print("\n--- REAL-WORLD EXAMPLE: GRADES ---")
grades = [88, 92, 79, 93, 85]
average = sum(grades) / len(grades)
print(f"Average grade: {average:.1f}")

# Challenge: Find the highest and lowest grade in the list.


# SUMMARY
print("\n--- SUMMARY ---")
print("- Lists store multiple values in a single variable")
print("- Use indexing and slicing to access parts of a list")
print("- List methods let you add, remove, and modify elements")
print("- Loop over lists for processing")
print("- List comprehensions create new lists efficiently")
print("- Nested lists represent 2D data")
print("- Practice working with lists!")
