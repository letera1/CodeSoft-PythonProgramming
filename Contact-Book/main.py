import os
import platform
from colorama import Fore, init

# Initialize colorama for cross-platform color support
init(autoreset=True)

contacts_file = "contact.txt"


def pause():
    """Pause the program and wait for a key press."""
    if platform.system() == "Windows":
        from msvcrt import getch
        getch()
    else:
        input("Press Enter to continue...")


def add_contact():
    """Add new contacts until the user decides to stop."""
    contacts = load_contacts()  # Load existing contacts

    while True:
        # Input new contact details
        name = input(Fore.YELLOW + "Enter the name: ").strip()
        phone_number = input(Fore.YELLOW + "Enter the phone number: ").strip()

        # Check for duplicate name or phone number
        if any(contact_name.lower() == name.lower() for contact_name in contacts):
            print(Fore.RED + "This name is already taken.")
        elif any(contact_number == phone_number for contact_number in contacts.values()):
            print(Fore.RED + "This phone number is already taken.")
        else:
            # Add and save the new contact
            contacts[name] = phone_number
            save_contacts(contacts)
            print(Fore.LIGHTGREEN_EX + "Contact added successfully.")

        # Ask if the user wants to add another contact
        choice = input(Fore.YELLOW + "Do you want to add another contact? (yes/no): ").strip().lower()
        if choice not in ('yes', 'y'):
            break

    after_task_prompt()


def show_contacts():
    """Display all contacts."""
    contacts = load_contacts()

    if not contacts:
        print(Fore.RED + "No contacts found.")
    else:
        print(Fore.LIGHTWHITE_EX + "Contacts:")
        for name, phone_number in sorted(contacts.items()):
            print(Fore.BLUE + f"{name} : {Fore.LIGHTMAGENTA_EX}{phone_number}")
    after_task_prompt()


def load_contacts():
    """Load contacts from the file into a dictionary."""
    contacts = {}
    if os.path.exists(contacts_file):
        with open(contacts_file, 'r') as f:
            for line in f:
                if " : " in line:
                    name, phone_number = line.strip().split(" : ")
                    contacts[name] = phone_number
    return contacts


def save_contacts(contacts):
    """Save contacts from a dictionary to the file."""
    with open(contacts_file, 'w') as f:
        for name, phone_number in sorted(contacts.items()):
            f.write(f"{name} : {phone_number}\n")


def after_task_prompt():
    """Prompt user to either return to main menu or exit the system."""
    while True:
        print(Fore.YELLOW + "\nWhat would you like to do next?")
        print(Fore.LIGHTWHITE_EX + "1. Return to Main Menu")
        print(Fore.LIGHTWHITE_EX + "2. Exit the System")
        choice = input(Fore.YELLOW + "Enter your choice: ").strip()
        if choice == '1':
            return  # Go back to the main menu
        elif choice == '2':
            print(Fore.LIGHTGREEN_EX + "Thank you for using the Contact Manager. Goodbye!")
            exit()
        else:
            print(Fore.RED + "Invalid input. Please try again.")


def main_menu():
    """Main menu for the contact management system."""
    while True:
        os.system("cls" if platform.system() == "Windows" else "clear")
        print(Fore.LIGHTWHITE_EX + "             Welcome            ")
        print(Fore.LIGHTWHITE_EX + "          1. Add Contact        ")
        print(Fore.LIGHTWHITE_EX + "         2. Show Contacts       ")
        print(Fore.LIGHTWHITE_EX + "             3. Exit            ")

        choice = input(Fore.YELLOW + "Enter your choice: ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            show_contacts()
        elif choice == '3':
            print(Fore.LIGHTGREEN_EX + "Thank you for using the Contact Manager. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid input. Please try again.")
            pause()


if __name__ == "__main__":
    main_menu()
