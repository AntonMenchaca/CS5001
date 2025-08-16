# CS5001

# Module 1: Python Variables, Variable Assignment, Arithmetic Expressions, and Concatenation

Welcome to **Module 1** of the CS5001 course! In this module, we will cover the basics of Python, focusing on variables, arithmetic expressions, and string concatenation. By the end of this module, you will be able to create and manipulate variables, perform basic arithmetic, and concatenate strings in Python.

## Learning Objectives

By the end of Module 1, you will be able to:
1. Understand how to create **variables** in Python.
2. Perform **arithmetic operations** using Python's operators.
3. Use **string concatenation** to join strings together.
4. Write Python code to solve basic problems involving variables and arithmetic.

## Key Topics

1. **Python Variables**: Learn how to create variables to store data such as numbers and strings.
2. **Variable Assignment**: Assign values to variables and understand how to change their values.
3. **Arithmetic Expressions**: Use operators like `+`, `-`, `*`, `/` to perform arithmetic on numbers.
4. **String Concatenation**: Combine strings using the `+` operator.

## Practice Materials

This module includes several practice files to help you master the concepts:

###  Practice Files

- **`module-1.py`** - Main learning content with examples and mini-challenges
- **`module-1-practice-questions.py`** - 40+ practice questions organized by difficulty
- **`module-1-quiz.py`** - Comprehensive quiz to test your understanding

###  How to Practice

1. **Start with `module-1.py`** - Review the examples and complete the challenges
2. **Work through `module-1-practice-questions.py`** - Complete all sections at your own pace
3. **Take the quiz in `module-1-quiz.py`** - Test your knowledge with various question types

###  Practice Question Categories

- **Variable Assignment** - Learn to create and modify variables
- **Arithmetic Operations** - Practice calculations and mathematical expressions
- **String Concatenation** - Master combining text and variables
- **Real-world Applications** - Solve practical problems like calculating tips, grades, and receipts
- **Challenge Problems** - Advanced exercises for extra practice

###  Getting Help

- **No points or grades** - These are purely for practice and learning!
- **Push your completed code** to GitHub when you're done
- **Answer keys will be provided** after you submit your work
- Practice as much as you need - repetition builds confidence!

Remember: The goal is to understand the concepts, not to get everything perfect on the first try. Take your time and experiment with the code!


# How to Read and Use This GitHub Repo

Welcome to the course repository! This repo is organized to guide you through the modules of **CS5001: Intensive Foundations of Computer Science**. Each module has its own branch, and every branch contains notes, examples, and challenges for that specific module. Follow this guide to effectively navigate through the branches, pull down the repo, and run Python code on PyCharm.

## Navigating the Repo

Each branch corresponds to a specific day or module in the course. To access different modules:

# How to Read and Use This GitHub Repo

Welcome to the course repository! This repo is organized to guide you through the modules of **CS5001: Intensive Foundations of Computer Science**. Each module has its own branch, and every branch contains notes, examples, and challenges for that specific module. Follow this guide to effectively navigate through the branches, pull down the repo, and run Python code on PyCharm.

## Navigating the Repo

Each branch corresponds to a specific day or module in the course. To access different modules:

1. **Clone the Repository**:  
   First, clone this repo to your local machine if you haven't already. Run the following command in your terminal:
   ```bash
   git clone https://github.com/AntonMenchaca/CS5001.git
   cd cs5001
   
## Switch to a Branch for the Module:
Use the following command to change branches:

bash
```
Copy code:
git checkout <branch-name>
For example, if you're working on Module 2, switch to the module-2 branch:
```
bash
```
Copy code:
git checkout module-2
```
## Pull the Latest Changes:
Before starting, make sure your branch is up-to-date with the latest content by pulling changes:

bash
```
Copy code:
git pull
```
## View the Module Content:
Inside each branch, you'll find:

## Notes: Documentation on the concepts covered in that module.
Examples: Python code examples to illustrate key concepts.
Challenges: Programming exercises to help you practice what you've learned.

## Running Python Code in PyCharm
Follow these steps to run the Python code for each module in PyCharm:

### Open PyCharm:
If you don't have it installed, download and install PyCharm.

### Open the Project:

1. In PyCharm, go to File > Open.
Select the folder where you cloned the GitHub repository.
## Set Up the Python Interpreter:

2. Go to File > Settings (or PyCharm > Preferences on macOS).
Select Project: <your project> > Python Interpreter.
Ensure Python 3.x is selected as your interpreter.
## Running the Code:

3. Right-click on the Python file you want to run.
Select Run '<filename>' to execute the script.
Alternatively, you can open the terminal in PyCharm and run:

bash
```
Copy code
python <filename>.py
```
### Commenting and Uncommenting Code
You may encounter Python files where certain parts of the code are commented out. Here's how to comment/uncomment sections of code:

### Commenting:
To comment out a line or section of code, use the # symbol at the beginning of the line:

python
```
Copy code
# This line is commented out and won't run.
You can also select multiple lines in PyCharm and press Ctrl + / (Windows/Linux) or Cmd + / (macOS) to comment or uncomment them.
```
### Uncommenting:
To uncomment a line, simply remove the # symbol:

python
```
Copy code
print("This line will run now!")
You can also select commented lines and press Ctrl + / (Windows/Linux) or Cmd + / (macOS) to quickly uncomment them.
```
## The Importance of Indentation and Spaces in Python Programming

In Python, **indentation** (the use of spaces or tabs at the beginning of lines) is critical to the structure and readability of your code. Unlike many other programming languages that use braces `{}` or keywords like `begin` and `end` to define code blocks, Python uses indentation to indicate a block of code. This makes Python more readable but also requires you to be precise with indentation.

### Why Indentation Matters

### 1. **Indicates Code Blocks**
Indentation in Python is used to define the structure of your code. For example, code blocks following `if` statements, loops, and functions must be indented. Without proper indentation, Python will throw an error.

### Example:
```python
if 5 > 3:
    print("5 is greater than 3")  # This line is indented and part of the 'if' block
print("This is outside the if block")  # This line is not indented and outside the 'if' block
```

## Troubleshooting
### Branch not found? Make sure you typed the branch name correctly. You can list all available branches by running:
bash
```

Copy code
git branch -a
```
### Python interpreter issues? Ensure that you’ve selected the correct version of Python (3.x) in PyCharm's settings.
That's it! You're all set to work through the modules. Be sure to check for any new branches and pull the latest changes before starting a new module. Happy coding!

## Resources

[Python Syntax Cheat Sheet.pdf](https://github.com/user-attachments/files/16944791/Python%2BSyntax%2BCheat%2BSheet%2BBooklet%2Bv2.pdf)

[W3 website for Python](https://www.w3schools.com/python/)

[Python Practice with Geeks for Geeks](https://www.geeksforgeeks.org/python-exercises-practice-questions-and-solutions/?ref=shm)


