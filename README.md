# Module 4: Functions, Parameters, Return Values, and Scope

Welcome to **Module 4** of the CS5001 course! In this module, you will learn how to write and use functions in Python. Functions help you organize code, avoid repetition, and make your programs easier to read and maintain.

## Learning Objectives

By the end of Module 4, you will be able to:
1. Define and call functions in Python.
2. Use parameters and arguments to pass data to functions.
3. Return values from functions and use them in your code.
4. Understand the difference between local and global variables (scope).
5. Use default and keyword arguments for flexibility.
6. Write functions that return multiple values.

## Key Topics

1. **Defining and Calling Functions**: Grouping code for reuse and clarity.
2. **Parameters and Arguments**: Passing data into functions.
3. **Return Values**: Sending data back from functions.
4. **Scope**: Local vs. global variables.
5. **Default and Keyword Arguments**: Flexible function calls.
6. **Returning Multiple Values**: Using tuples to return more than one result.
7. **Real-World Examples**: Practical uses of functions in programs.

## Practice Materials for Module 4

This module includes several practice files to help you master functions and scope:

###  Practice Files

- **`module-4.py`** – Main learning content with examples, best practices, and mini-challenges
- **`module-4-practice-questions.py`** – Practice questions organized by topic
- **`module-4-quiz.py`** – Practice quiz to test your understanding

###  How to Practice

1. **Start with `module-4.py`** – Review the examples and complete the challenges
2. **Work through `module-4-practice-questions.py`** – Complete all sections at your own pace
3. **Take the quiz in `module-4-quiz.py`** – Test your knowledge with various question types

###  Practice Question Categories

- Defining and Calling Functions
- Parameters and Arguments
- Return Values
- Scope (Local vs Global)
- Default and Keyword Arguments
- Returning Multiple Values
- Real-World Scenarios & Challenges

###  Getting Help

- **No points or grades** – These are purely for practice and learning!
- **Push your completed code** to GitHub when you're done
- **Answer keys will be provided** after you submit your work
- Practice as much as you need – repetition builds confidence!

Remember: The goal is to understand the concepts, not to get everything perfect on the first try. Take your time and experiment with the code!




7. **Evaluate Efficiency of Code**  
   Assess the impact of data structure and algorithm choices on both run time and memory usage, ensuring efficient program execution.

## Getting Started

1. **Programming Language**: Python 3.x
2. **Prerequisites**: No prior programming experience is necessary.
3. **Tools**: 
   - Python IDE (PyCharm, VSCode, etc.)
   - Version control with Git
4. **Course Materials**: 
   - Textbooks, lecture notes, and online resources will be provided.

## Grading and Assessment

1. **Homework Assignments** (40%) - Small coding exercises and problem sets.
2. **Projects** (30%) - Larger programming projects that apply course concepts.
3. **Quizzes** (10%) - Short assessments to test your understanding of the material.
4. **Final Exam** (20%) - Cumulative exam covering key course topics.

## Course Policies

- **Late Submissions**: Assignments turned in late will incur a penalty unless prior arrangements are made.
- **Academic Integrity**: Collaboration on assignments is encouraged, but the work you submit must be your own. Ensure that you properly credit any external sources.


Good luck, and let's have a great semester learning how to think and solve problems like computer scientists!

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
