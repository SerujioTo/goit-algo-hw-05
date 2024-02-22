def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name found"
        except IndexError:
            return "Not found"
        except Exception as e:
            return f"Error: {e}"

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts.append({'name': name, 'phone': phone})
    return "Contact added."

@input_error
def show_phone(args, contacts):
    name = args[0]
    for contact in contacts:
        if contact["name"] == name:
            return contact["phone"]
    return 'Not found'

@input_error
def change_phone(args, contacts):
    name, phone = args
    # contacts.replace()
    for index, contact in enumerate(contacts):
        if contact["name"] == name:
            contacts[index] = {"name": name, "phone": phone}
            return "Contact is changed"
    return "Not found"

@input_error
def all_phones(args, contacts):
    contact_string = ""
    for contact in contacts:
        contact_string += f"{contact['name']}: {contact['phone']}\n"
    return contact_string


def main():
    contacts = [{'name': 'John Doe', 'phone': '+380988858880'},
                {'name': 'Alice Cooper', 'phone': '+48880884215'}]
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "all":
            print(all_phones(args, contacts), end="")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()