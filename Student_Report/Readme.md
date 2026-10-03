# Student Report System

## Description

Student Report System is a simple Python program that takes a student's name and marks in three subjects as input. It calculates the total marks, average marks, and determines whether the student has passed or failed.

This project is created using basic Python concepts such as functions, dictionaries, conditional statements, user input, and loops.

## Features

- Takes student name as input
- Takes marks for three subjects
- Calculates total marks
- Calculates average marks
- Checks pass or fail status
- Displays the student report

## Technologies Used

- Python
- Visual Studio Code

## Python Concepts Used

- Functions
- User Input
- Integer Data Type
- Arithmetic Operations
- Conditional Statements
- Dictionary
- For Loop
- Dictionary `items()` method

## How to Run in VS Code

1. Open Visual Studio Code.
2. Create a new folder named `Student-Report-System`.
3. Create a Python file named `student_report.py`.
4. Add the Python code to the file.
5. Open the VS Code terminal.
6. Run the following command:

```bash
python student_report.py
```

7. Enter the student name and marks when asked.

## Sample Input

```text
Enter the name: Uma
Enter the subjec1 marks: 95
Enter the subjec2 marks: 93
Enter the subjec3 marks: 97
```

## Sample Output

```text
Student Name : Uma
Total : 285
Average : 95
Result : Pass
```

## Project Structure

```text
Student-Report-System/
│
├── student_report.py
└── README.md
```

## Program Logic

The program uses three functions:

### Total

The `total()` function adds the marks of all three subjects.

### Average

The `average()` function calculates the average of the three subject marks.

### Result

The `Result()` function checks the average marks.

- If the average is 40 or above, the result is `Pass`.
- If the average is below 40, the result is `Fail`.

The final report is stored in a dictionary and displayed using a `for` loop.

## Future Improvements

- Add more subjects
- Add grade calculation
- Add marks validation
- Support multiple students
- Store student reports in a file
- Add a graphical user interface

## Author

Uma Naga Srinivas

B.Tech - Artificial Intelligence & Machine Learning