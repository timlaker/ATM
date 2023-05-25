import os

PIN = "1234"
balance = 1000

# create check balance function
def check_balance():
    global balance
    print(f"Current balance: {balance}")


# create change pin function
def change_pin():
    global PIN
    x = input("Enter a new PIN: ")
    y = input("Confirm new PIN: ")
    if x == y:
        PIN = y
        print("PIN successfully updated")
    else:
        print("Numbers entered do not match")
        

# create withdraw function
def withdraw(amount):
    global balance
    if amount >= balance:
        print("Insufficient funds, please try again")
    else:
        balance -= amount
        print(f"{amount} withdrawn, your new balance is {balance}")

# create deposit function
def deposit(amount):
    global balance
    balance += amount
    print(f"Successfully deposited {amount}, your new balance is {balance}")


while True:
    print()
    print("Welcome, please select from the following options:")
    print()
    print("1: Check your balance")
    print("2: PIN Services")
    print("3: Withdraw Cash")
    print("4: Deposit")
    print("5: Quit")
    print()


    option = input("Choose an option 1-5: ")
    
    if option == "1":
        os.system('cls')
        validation = input("Please enter your PIN: ")
        if validation == PIN:
            os.system('cls')
            check_balance()
            print()
            answer = input("Would you like another service? 1: Yes, 2: No: ")
            if answer == "1":
                continue
            else:
                os.system('cls')
            print("Thank you for using our service")
            break
        else:
            os.system('cls') 
            print("Incorrect PIN Entered")
    
    if option == "2":
        os.system('cls')
        validation = input("Please enter your PIN: ")
        if validation == PIN:
            os.system('cls')
            change_pin()
            print()
            answer = input("Would you like another service? 1: Yes, 2: No: ")
            if answer == "1":
                continue
            else:
                os.system('cls')
            print("Thank you for using our service")
            break
        else:
            os.system('cls')
            print("Incorrect PIN Entered")
        
    if option == "3":
        os.system('cls')
        validation = input("Please enter your PIN: ")
        if validation == PIN:
            os.system('cls')
            amount = float(input("How much would you like to withdraw?: "))
            os.system('cls')
            withdraw(amount)
            print()
            answer = input("Would you like another service? 1: Yes, 2: No: ")
            if answer == "1":
                continue
            else:
                os.system('cls')
            print("Thank you for using our service")
            break
        else:
            os.system('cls')
            print("Incorrect PIN Entered")
        
    if option == '4':
        os.system('cls')
        validation = input("Please enter your PIN: ")
        if validation == PIN:
            os.system('cls')
            deposit_amount = float(input("How much would you like to deposit?: "))
            os.system('cls')
            deposit(deposit_amount)
            print()
            answer = input("Would you like another service? 1: Yes, 2: No: ")
            if answer == "1":
                continue
            else:
                os.system('cls')
            print("Thank you for using our service")
            break
        else:
            os.system('cls')
            print("Incorrect PIN Entered")
    
    if option == "5":
        os.system('cls')
        print("Thank you for using our service")
        break
    elif option < "1" or option > "4":
        os.system('cls')
        option = input("Choose an option 1-5: ")