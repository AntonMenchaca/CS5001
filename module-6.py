### MODULE 6 ###
# Dictionaries, Key-Value Pairs, and Dictionary Methods

# DICTIONARY BASICS
print("\n--- DICTIONARY BASICS ---")
student = {"name": "Alice", "age": 20, "major": "CS"}
print(student)

# Accessing values by key
print(student["name"])
print(student.get("age"))

# Challenge: Print the value for the key 'major'.


# ADDING AND REMOVING ITEMS
print("\n--- ADDING AND REMOVING ITEMS ---")
student["gpa"] = 3.8
print(student)
del student["age"]
print(student)

# Challenge: Add a new key-value pair and then remove a different key.


# LOOPING OVER DICTIONARIES
print("\n--- LOOPING OVER DICTIONARIES ---")
for key in student:
    print(key, student[key])

for key, value in student.items():
    print(f"{key}: {value}")

# Challenge: Print all keys in a dictionary.


# COMMON DICTIONARY METHODS
print("\n--- COMMON DICTIONARY METHODS ---")
print(student.keys())
print(student.values())
print(student.items())

# Challenge: Use .get() to safely access a key that might not exist.


# NESTED DICTIONARIES
print("\n--- NESTED DICTIONARIES ---")
classroom = {
    "student1": {"name": "Bob", "grade": 90},
    "student2": {"name": "Sue", "grade": 85}
}
print(classroom["student1"]["name"])

# Challenge: Print the grade for 'student2'.


# REAL-WORLD EXAMPLE: WORD COUNTER
print("\n--- REAL-WORLD EXAMPLE: WORD COUNTER ---")
text = "hello world hello python"
word_counts = {}
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(word_counts)

# Challenge: Count the frequency of each letter in a string.


# SUMMARY
print("\n--- SUMMARY ---")
print("- Dictionaries store data as key-value pairs")
print("- Use keys to access, add, or remove values")
print("- Loop over dictionaries for processing")
print("- Use dictionary methods for common tasks")
print("- Nested dictionaries represent complex data")
print("- Practice working with dictionaries!")
