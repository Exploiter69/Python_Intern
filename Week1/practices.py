import math

# 1. Area of a circle
def area_of_circle(radius):
    return math.pi * (radius ** 2)

# 2. Even or Odd
def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# 3. Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 4. Count vowels and consonants
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

# 5. Fibonacci sequence up to n terms
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example usage:
# print(area_of_circle(5))
# print(check_even_odd(10))
# print(factorial(5))
# print(count_vowels_consonants("Hello"))
# fibonacci(5)