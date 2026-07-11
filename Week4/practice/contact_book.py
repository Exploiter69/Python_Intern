contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Added {name}.")

def search_contact(name):
    print(contacts.get(name, "Contact not found."))

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name}.")
    else:
        print("Contact not found.")

# Example usage:
# add_contact("Alok", "9876543210")
# search_contact("Alok")