import handler
from handler import PhonebookError


def parse_user_input(user_input: str) -> tuple:
    command, *arguments = user_input.split()
    command = command.strip().lower()
    return command, *arguments


def main():
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *arguments = parse_user_input(user_input)

        if command == "hello":
            print("How can I help you?")

        elif command == "all":
            contacts = handler.list_all_contacts()
            print(contacts)

        elif command == "add":
            try:
                name, phone = arguments
                handler.add_entry(name, phone)
            except PhonebookError as e:
                print(e)
                continue
            except ValueError:
                print("Invalid command. Usage: add [name] [phone_number]")
                continue

            print("Contact added.")

        elif command == "change":
            try:
                name, phone = arguments
                handler.update_entry(name, phone)
            except PhonebookError as e:
                print(e)
                continue
            except ValueError:
                print("Invalid command. Usage: change [name] [new_phone_number]")
                continue

            print("Contact updated.")

        elif command == "phone":
            try:
                name = arguments[0]
                phone = handler.get_phone(name)
                print(phone)
            except PhonebookError as e:
                print(e)
                continue
            except (ValueError, IndexError):
                print("Invalid command. Usage: phone [name]")
                continue

        elif command in ["exit", "close"]:
            print("Goodbye!")
            break

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
