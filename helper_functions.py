def validate_input(user_input):
    """
    Validates that the user input is not empty and is a string.
    Returns True if valid, otherwise False.
    """
    if isinstance(user_input, str) and user_input.strip() != "":
        return True
    return False


def convert_to_binary(text):
    """
    Converts text or number to binary.
    If it's a string, convert each character to its ASCII binary value.
    If it's a number, convert it using bin().
    """
    if text.isdigit():  # Check if text is numeric (like age)
        return bin(int(text))
    else:
        return " ".join(format(ord(char), '08b') for char in text)


def create_message(name, age, name_binary, age_binary):
    """
    Creates a personalized message combining all details.
    """
    message = (
        f"Hello {name}, you are {age} years old!\n"
        f"Name in binary: {name_binary}\n"
        f"Age in binary: {age_binary}"
    )
    return message

