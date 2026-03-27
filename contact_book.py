# ============================================================
#   📒 CONTACT BOOK — A Python OOP Project
#   Author  : Nischal Koirala
#   Purpose : Manage contacts using Object-Oriented Programming
# ============================================================
#
#   CONCEPTS USED IN THIS PROJECT:
#   ✅ Classes and Objects
#   ✅ __init__ method (constructor)
#   ✅ Instance methods
#   ✅ Encapsulation (keeping data inside a class)
#   ✅ List to store multiple objects
#   ✅ User input and a simple menu
#
# ============================================================


# ── CLASS 1: Contact ─────────────────────────────────────────
# A "Contact" is a blueprint for storing one person's details.
# Every contact we create will have a name, phone, and email.

class Contact:

    def __init__(self, name, phone, email):
        """
        __init__ runs automatically when we create a new Contact.
        It sets up the contact's data (name, phone, email).
        """
        self.name  = name    # The contact's full name
        self.phone = phone   # The contact's phone number
        self.email = email   # The contact's email address

    def display(self):
        """
        Prints the contact's details in a readable format.
        """
        print(f"""
  👤  Name  : {self.name}
  📞  Phone : {self.phone}
  📧  Email : {self.email}
  {"─" * 35}""")


# ── CLASS 2: ContactBook ──────────────────────────────────────
# The ContactBook manages a list of Contact objects.
# It can add, search, delete, and display contacts.

class ContactBook:

    def __init__(self):
        """
        Creates an empty list to hold all contacts.
        """
        self.contacts = []   # This list will store Contact objects

    def add_contact(self, name, phone, email):
        """
        Creates a new Contact object and adds it to the list.
        """
        new_contact = Contact(name, phone, email)   # Create the object
        self.contacts.append(new_contact)            # Add to list
        print(f"\n  ✅ Contact '{name}' added successfully!")

    def view_all(self):
        """
        Displays every contact in the contact book.
        """
        if len(self.contacts) == 0:
            print("\n  📭 Your contact book is empty.")
            return

        print(f"\n  📒 You have {len(self.contacts)} contact(s):\n")
        print("  " + "─" * 35)
        for contact in self.contacts:
            contact.display()

    def search_contact(self, search_name):
        """
        Searches for a contact by name (case-insensitive).
        """
        found = False
        for contact in self.contacts:
            if search_name.lower() in contact.name.lower():
                contact.display()
                found = True

        if not found:
            print(f"\n  ❌ No contact found with the name '{search_name}'.")

    def delete_contact(self, search_name):
        """
        Removes a contact from the list by name.
        """
        for contact in self.contacts:
            if contact.name.lower() == search_name.lower():
                self.contacts.remove(contact)
                print(f"\n  🗑️  Contact '{contact.name}' deleted.")
                return

        print(f"\n  ❌ No contact named '{search_name}' was found.")

    def total_contacts(self):
        """
        Returns how many contacts are saved.
        """
        return len(self.contacts)


# ── HELPER FUNCTION: Print the menu ──────────────────────────

def print_menu():
    print("""
  ╔══════════════════════════════════╗
  ║        📒 MY CONTACT BOOK        ║
  ╠══════════════════════════════════╣
  ║  1 → Add a new contact           ║
  ║  2 → View all contacts           ║
  ║  3 → Search a contact            ║
  ║  4 → Delete a contact            ║
  ║  5 → Exit                        ║
  ╚══════════════════════════════════╝
    """)


# ── MAIN PROGRAM ─────────────────────────────────────────────
# This is where the program starts running.

def main():

    # Create a ContactBook object — our "database"
    book = ContactBook()

    # Add a few sample contacts so it isn't empty at start
    book.add_contact("John Cena",  "9841000001", "cena@email.com")
    book.add_contact("Jane Doe",   "9841000002", "jane@email.com")
    book.add_contact("John Doe",   "9841000003", "john@email.com")

    print("\n  👋 Welcome to your Contact Book!")

    # ── Main loop: keep showing the menu until user exits ──
    while True:

        print_menu()
        choice = input("  Enter your choice (1-5): ").strip()

        # ── Option 1: Add contact ──
        if choice == "1":
            print("\n  ── Add New Contact ──")
            name  = input("  Enter name  : ").strip()
            phone = input("  Enter phone : ").strip()
            email = input("  Enter email : ").strip()

            if name and phone and email:
                book.add_contact(name, phone, email)
            else:
                print("\n  ⚠️  All fields are required. Please try again.")

        # ── Option 2: View all contacts ──
        elif choice == "2":
            book.view_all()

        # ── Option 3: Search contact ──
        elif choice == "3":
            print("\n  ── Search Contact ──")
            name = input("  Enter name to search: ").strip()
            book.search_contact(name)

        # ── Option 4: Delete contact ──
        elif choice == "4":
            print("\n  ── Delete Contact ──")
            name = input("  Enter exact name to delete: ").strip()
            book.delete_contact(name)

        # ── Option 5: Exit ──
        elif choice == "5":
            print(f"\n  👋 Goodbye! You had {book.total_contacts()} contact(s) saved.\n")
            break

        # ── Invalid input ──
        else:
            print("\n  ⚠️  Invalid choice. Please enter a number from 1 to 5.")


# Run the program
if __name__ == "__main__":
    main()
