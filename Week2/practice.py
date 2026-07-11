# 1. Create a list and perform CRUD operations
my_list = [10, 20, 30]
my_list.append(40)      # Create
print(my_list[0])       # Read
my_list[1] = 25         # Update
my_list.pop()           # Delete
print("CRUD List:", my_list)

# 2. Dictionary program to count word frequency
text = "apple banana apple orange banana apple"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word Frequency:", freq)

# 3. Use nested loops to print a pattern
print("Pattern:")
for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()

# 4. Find largest and smallest number in a list
nums = [15, 3, 78, 1, 99]
print(f"Largest: {max(nums)}, Smallest: {min(nums)}")

# 5. Sort a list using sort() and lambda key
# Example: Sort a list of tuples by the second element
data = [("apple", 5), ("banana", 2), ("cherry", 8)]
data.sort(key=lambda x: x[1])
print("Sorted by value:", data)