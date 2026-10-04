# Expense Tracker

## Description

Expense Tracker is a simple Python-based program that allows users to enter their expenses and calculate the total amount spent.

The program continues accepting expenses until the user types `stop`. It also handles invalid inputs using exception handling and displays a message when no expenses are recorded.

## Features

- Allows users to enter multiple expenses
- Stops input when the user types `stop`
- Stores expenses in a list
- Calculates the total amount spent
- Handles invalid numerical input
- Displays all recorded expenses
- Displays a message when no expenses are recorded

## Technologies Used

- Python
- Visual Studio Code

## Python Concepts Used

- Lists
- User Input
- `while` loop
- `if-else` statements
- `break` statement
- `try-except`
- `ValueError`
- `int()` type conversion
- `sum()` function
- List `append()` method

## How to Run

1. Open Visual Studio Code.
2. Open the project folder.
3. Create or open the Python file.
4. Run the Python program.
5. Enter the expense amount when asked.
6. Type `stop` to finish entering expenses.

## Project Structure

Expense_Tracker/
│
├── expense_tracker.py
└── README.md

## Program Logic

1. Create an empty list to store expenses.
2. Ask the user to enter an expense.
3. If the user enters `stop`, exit the loop.
4. Convert the entered value into an integer.
5. Add the expense to the list.
6. If the input is invalid, display an error message.
7. Calculate the total using the `sum()` function.
8. Display the recorded expenses and total amount.
9. If no expenses were entered, display `no expenses recorded`.

## Sample Output

### Example 1: Expenses Recorded

Enter an expense (or type stop): 600
Enter an expense (or type stop): 200
Enter an expense (or type stop): 200
Enter an expense (or type stop): hfdk
Invalid input: please enter the numerical input
Enter an expense (or type stop): stop

Your Expences are: [600, 200, 200]
Total Spent: 1000

### Example 2: No Expenses

Enter an expense (or type stop): stop

no expenses recorded

## Future Improvements

- Add expense categories
- Add dates for expenses
- Calculate average spending
- Add monthly expense reports
- Store expenses in a file
- Add a graphical user interface
- Add options to edit or delete expenses

## Author

**Uma Naga Srinivas**

B.Tech - Artificial Intelligence & Machine Learning