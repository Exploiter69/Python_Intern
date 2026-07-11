# 1. Bank Account Class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance: self.balance -= amount
    def display_balance(self):
        print(f"Balance: {self.balance}")

# 2. Library Management System (OOP)
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book): self.books.append(book)
    def issue_book(self, book):
        if book in self.books: self.books.remove(book)

# 3. Calculator Class with Exception Handling
class Calculator:
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Cannot divide by zero"