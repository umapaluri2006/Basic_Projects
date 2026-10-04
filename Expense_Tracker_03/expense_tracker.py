Expenses = []
while True:
    amount = input("Enter an expense (or type stop):")
    if amount == 'stop':
        break
    try:
        expence = int(amount) 
        Expenses.append(expence)
    except ValueError:
        print("Invalid input: please enter the numerical input")

total = sum(Expenses)
if not Expenses:
    print("no expenses recorded")
else:
    print("Your Expences are:",Expenses)
    print("Total Spent:",total)


# Output:

# Enter an expense (or type stop):600
# Enter an expense (or type stop):200
# Enter an expense (or type stop):200
# Enter an expense (or type stop):hfdk
# Invalid input: please enter the numerical input
# Enter an expense (or type stop):stop
# Your Expences are: [200, 600, 200]
# Total Spent: 1000


# Enter an expense (or type stop):stop
# no expenses recorded