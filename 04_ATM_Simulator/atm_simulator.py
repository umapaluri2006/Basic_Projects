balance = 1000
def check_balance():
    print("Current Balance:",balance)
def deposit():
    global balance
    depoamount = int(input("Enter deposit amount:"))
    balance += depoamount
    print("Deposit Successful!")                        
def withdraw():
    global balance
    withamount = int(input("Enter withdraw amount:"))
    if balance >= withamount:
        balance -= withamount
        print("Withdraw Successful!")
    else:
        print("Insufficient Balance!")
while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice:")
    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        print("Thank you! Goodbye.")
        break
    else:
        print("Invalid Choice!")



#Output:
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
# Enter your choice:1
# Current Balance: 1000
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
# Enter your choice:2
# Enter deposit amount:10000
# Deposit Successful!
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
# Enter your choice:3
# Enter withdraw amount:1000
# Withdraw Successful!
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
# Enter your choice:1
# Current Balance: 10000
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
# Enter your choice:4
# Thank you! Goodbye.