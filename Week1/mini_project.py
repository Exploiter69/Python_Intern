# --- Mini Project: ATM Simulator ---
balance = 1000  # Initial balance
PIN = "1234"    # Predefined PIN

def check_balance():
    print(f"Your current balance is: ${balance}")

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ${amount}. New balance: ${balance}")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew ${amount}. New balance: ${balance}")
    else:
        print("Insufficient funds!")

# User Login
user_pin = input("Enter PIN: ")
if user_pin == PIN:
    while True:
        choice = input("\n1: Balance, 2: Deposit, 3: Withdraw, 4: Exit. Select: ")
        if choice == '1': check_balance()
        elif choice == '2': deposit(float(input("Amount: ")))
        elif choice == '3': withdraw(float(input("Amount: ")))
        elif choice == '4': break
else:
    print("Invalid PIN.")