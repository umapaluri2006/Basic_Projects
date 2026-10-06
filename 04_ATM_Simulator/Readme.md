# ATM Simulator

## Description

ATM Simulator is a simple Python-based program that simulates basic ATM operations.

The program starts with an initial balance and allows the user to check their balance, deposit money, withdraw money, and exit the program through a menu-driven system.

## Features

- Displays the current account balance
- Allows users to deposit money
- Allows users to withdraw money
- Checks for sufficient balance before withdrawal
- Displays an insufficient balance message when required
- Provides a menu-driven interface
- Allows users to exit the program

## Technologies Used

- Python
- Visual Studio Code

## Python Concepts Used

- Variables
- Functions
- Global variables
- `global` keyword
- User Input
- `if-elif-else` statements
- `while` loop
- `break` statement
- Integer type conversion using `int()`
- Arithmetic operations
- Comparison operators

## How to Run

1. Open Visual Studio Code.
2. Open the project folder.
3. Open the Python file.
4. Run the Python program.
5. Select an option from the displayed menu.
6. Enter the required amount for deposit or withdrawal.
7. Select option `4` to exit the program.

## Project Structure

ATM_Simulator/
│
├── atm_simulator.py
└── README.md

## Program Logic

1. Start with an initial balance of `1000`.
2. Display the ATM menu.
3. Ask the user to enter their choice.
4. If the user selects `1`, display the current balance.
5. If the user selects `2`, ask for a deposit amount and add it to the balance.
6. If the user selects `3`, ask for a withdrawal amount.
7. Check whether the balance is sufficient for the withdrawal.
8. If sufficient, subtract the withdrawal amount from the balance.
9. If insufficient, display `Insufficient Balance!`.
10. If the user selects `4`, exit the program.
11. Display `Invalid Choice!` for an invalid menu option.

## Sample Output

### Example: ATM Operations

1. Check Balance
2. Deposit
3. Withdraw
4. Exit

Enter your choice: 1

Current Balance: 1000

1. Check Balance
2. Deposit
3. Withdraw
4. Exit

Enter your choice: 2

Enter deposit amount: 10000

Deposit Successful!

1. Check Balance
2. Deposit
3. Withdraw
4. Exit

Enter your choice: 3

Enter withdraw amount: 1000

Withdraw Successful!

1. Check Balance
2. Deposit
3. Withdraw
4. Exit

Enter your choice: 1

Current Balance: 10000

1. Check Balance
2. Deposit
3. Withdraw
4. Exit

Enter your choice: 4

Thank you! Goodbye.

## Future Improvements

- Add PIN authentication
- Add transaction history
- Add withdrawal limits
- Add multiple account support
- Add input validation for negative amounts
- Store account details using files or a database
- Add a graphical user interface

## Author

**Uma Naga Srinivas**

B.Tech - Artificial Intelligence & Machine Learning