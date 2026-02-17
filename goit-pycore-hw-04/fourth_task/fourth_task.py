def parse_input(user_input):
    """Parses user input into command and arguments. Case-insensitive."""
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


def add_contact(args, contacts):
    """Adds a new contact to the dictionary. Expects args: [name, phone]."""
    if len(args) < 2:
        return "Invalid command."
    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Updates phone number for an existing contact. Expects args: [name, new_phone]."""
    if len(args) < 2:
        return "Invalid command."
    name, phone = args[0], args[1]
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    """Returns phone number for the specified contact. Expects args: [name]."""
    if len(args) < 1:
        return "Invalid command."
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]


def show_all(args, contacts):
    """Returns a string with all saved contacts."""
    if not contacts:
        return "No contacts saved."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
