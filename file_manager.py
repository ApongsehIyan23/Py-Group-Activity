def save_message(message):
    """
    Saves the given message to user_message.txt.
    Handles file write errors gracefully.
    """
    try:
        with open("user_message.txt", "w") as file:
            file.write(message)
        print("Message saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the message: {e}")


def read_message():
    """
    Reads the message from user_message.txt and prints it.
    Handles file read errors gracefully.
    """
    try:
        print("Reading saved message...")
        with open("user_message.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("No saved message found.")
    except Exception as e:
        print(f"An error occurred while reading the message: {e}")

