# --- Assignment 1: Temperature Converter ---
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# --- Assignment 2: Student Grade Calculator ---
def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90: grade = 'A'
    elif avg >= 80: grade = 'B'
    elif avg >= 70: grade = 'C'
    else: grade = 'F'
    return avg, grade

# --- Assignment 3: Even/Odd & Prime Checker ---
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# Example Usage
print(f"100C to F: {celsius_to_fahrenheit(100)}")
print(f"Grade for [85, 90, 95]: {calculate_grade([85, 90, 95])}")
print(f"Is 7 prime? {is_prime(7)}")