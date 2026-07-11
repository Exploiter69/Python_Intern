import pandas as pd
import matplotlib.pyplot as plt
import json

# 1. Read a file and count total lines
def count_lines(filename):
    with open(filename, 'r') as f:
        return len(f.readlines())

# 2. Write a program to merge two text files
def merge_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data = f1.read() + "\n" + f2.read()
    with open(output_file, 'w') as out:
        out.write(data)

# 3. Use Pandas to load and analyze a CSV file
# Assuming you have a file named 'data.csv'
def analyze_csv(filename):
    df = pd.read_csv(filename)
    print(df.head()) # Shows first 5 rows
    print(df.describe()) # Basic statistical analysis

# 4. Use Matplotlib to plot a line graph
def plot_graph():
    x = [1, 2, 3, 4]
    y = [10, 20, 25, 30]
    plt.plot(x, y)
    plt.title("Sample Line Graph")
    plt.show()

# 5. Create a JSON file and read data from it
def json_operations():
    data = {"name": "Alok", "role": "Intern"}
    # Create/Write
    with open('data.json', 'w') as f:
        json.dump(data, f)
    # Read
    with open('data.json', 'r') as f:
        print(json.load(f))