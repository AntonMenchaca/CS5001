# CS5001
Northeastern 5001 notes
# Table of Contents

1. [CS5001: Intensive Foundations of Computer Science](#cs5001-intensive-foundations-of-computer-science)
   - [Course Objectives](#course-objectives)
   - [Getting Started](#getting-started)
   - [Grading and Assessment](#grading-and-assessment)
   - [Course Policies](#course-policies)
   - [Contact Information](#contact-information)

2. [How to Read and Use This GitHub Repo](#how-to-read-and-use-this-github-repo)
   - [Navigating the Repo](#navigating-the-repo)
   - [Switch to a Branch for the Module](#switch-to-a-branch-for-the-module)
   - [Pull the Latest Changes](#pull-the-latest-changes)
   - [View the Module Content](#view-the-module-content)

3. [Running Python Code in PyCharm](#running-python-code-in-pycharm)
   - [Open PyCharm](#open-pycharm)
   - [Open the Project](#open-the-project)
   - [Set Up the Python Interpreter](#set-up-the-python-interpreter)
   - [Running the Code](#running-the-code)

4. [Commenting and Uncommenting Code](#commenting-and-uncommenting-code)
   - [Commenting](#commenting)
   - [Uncommenting](#uncommenting)
     
5. [The Importance of Indentation and Spaces in Python Programming](#the-importance-of-indentation-and-spaces-in-python-programming)
   - [Why Indentation Matters](#why-indentation-matters)

7. [Troubleshooting](#troubleshooting)


# CS5001: Intensive Foundations of Computer Science

Welcome to **CS5001: Intensive Foundations of Computer Science** at Northeastern University. This course introduces the foundational concepts of computer science and programming using Python. Through this class, students will learn how to analyze problems, design solutions, and write efficient, well-documented code.

## Course Objectives

By the end of this course, students will be able to:

1. **Analyze and Solve Large Problems**  
   Develop a basic understanding of how to break down large problems into smaller, manageable components and implement efficient solutions using the Python programming language.

2. **Understand and Trace Code**  
   Determine the functionality of code written by oneself and others through reading and tracing short segments of code.

3. **Write Readable and Documented Programs**  
   Write correct, readable, and well-documented small-to-medium sized programs that others can easily understand and modify.

4. **Limit Code Duplication**  
   Use generalization for data and functions to minimize redundancy in code.

5. **Develop Effective Tests**  
   Develop tests to thoroughly exercise your implemented code, ensuring robust software development and high-quality testing processes.

6. **Select Appropriate Data Types**  
   Choose appropriate data types to represent information, including utilizing common Python library classes.

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

## Contact Information

- **Instructor**: [Instructor Name]
- **Office Hours**: [Times]
- **Email**: [Instructor Email]

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
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
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
