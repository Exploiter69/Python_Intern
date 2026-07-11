import json

# 1. Contact Book using Dictionary
contact_book = {}

def manage_contacts(action, name, phone=None):
    if action == "add": contact_book[name] = phone
    elif action == "update": contact_book[name] = phone
    elif action == "delete": contact_book.pop(name, None)
    elif action == "search": return contact_book.get(name, "Not Found")
    return contact_book

# 2. Word Counter from Text File
def count_file_stats(filename):
    with open(filename, 'r') as f:
        content = f.read()
        lines = content.splitlines()
        words = content.split()
        chars = len(content)
        return len(lines), len(words), chars

# 3. JSON File Reader
def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        print(json.dumps(data, indent=4))