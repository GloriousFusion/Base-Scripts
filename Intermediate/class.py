account = None

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def info(self):
        print(
f"""
- User Information
- Name: {self.name}
- Password: {self.password}
""")

    def info_reverse(self):
        print(
f"""
- User Information
- Name: {self.name}
- Password: {self.password}
"""[::-1])


def user_input():
    try:
        prompt = input("> ")
        return prompt
    except KeyboardInterrupt:
        print("Quitting: User Input!")
        quit()
        # return "exit"


def user_commands():
    print("Type a command")
    active = True

    while active:
        command = user_input()

        if command == "info":
            User.info(account)

        elif command == "reverse":
            User.info_reverse(account)

        # ...

        elif command == "exit":
            print("Quitting: User Commands!")
            active = False
            # break


def account_creation():
    global account # Can be improved by using a txt/json file to access, edit and store data into such variable instead of calling global

    account_name = "Default"
    account_password = "password"

    if account is None: # Improved method = from 'account_data' file read and check if this data is empty or not
        print("No account detected, want to create one? (Enter a name or press enter for 'Default')")
        name = user_input()

        if name.strip() != "":
            account_name = name

        print("Create a password (press enter for default password = 'password')")
        password = user_input()

        if password.strip() != "":
            account_password = password

        account = User(account_name, account_password) # Improved method = write data into 'account_data' file
        print("Account created!")

    user_commands()


if __name__ == "__main__": # Executes only if the script is run directly, and not when imported by another script
    print("Running as main program!")
    account_creation()