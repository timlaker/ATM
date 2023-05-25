balance = 1000
pin = '1234'  # user's PIN

def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
        print("Withdrawal successful. Remaining balance is", balance)
    else:
        print("Insufficient funds.")

def deposit(amount):
    global balance
    balance += amount
    print("Deposit successful. Remaining balance is", balance)

# main program loop
while True:
    print("Welcome to the cash machine.")
    print("1. Withdraw money")
    print("2. Deposit money")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        pin_input = input("Enter your PIN: ")
        if pin_input == pin:
            amount = float(input("Enter the amount to withdraw: "))
            withdraw(amount)
        else:
            print("Incorrect PIN. Please try again.")
    elif choice == '2':
        pin_input = input("Enter your PIN: ")
        if pin_input == pin:
            amount = float(input("Enter the amount to deposit: "))
            deposit(amount)
        else:
            print("Incorrect PIN. Please try again.")
    elif choice == '3':
        print("Thank you for using the cash machine.")
        break
    else:
        print("Invalid choice. Please try again.")
