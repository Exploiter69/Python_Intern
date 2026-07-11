import csv
import os

FILE = "students.csv"

def save_data(data):
    with open(FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def load_data():
    if not os.path.exists(FILE): return []
    with open(FILE, 'r') as f:
        return list(csv.reader(f))

def add_student(name, marks, roll):
    data = load_data()
    data.append([name, marks, roll])
    save_data(data)

def search_student(roll):
    for student in load_data():
        if student[2] == roll: return student
    return "Not Found"

def delete_student(roll):
    data = [s for s in load_data() if s[2] != roll]
    save_data(data)

# Example usage for the project:
# add_student("Alok", 95, "101")
# print(search_student("101"))
# delete_student("101")