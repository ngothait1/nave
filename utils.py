def printNotNumerError(field_name: str, user_input: str) -> None:
    print(f"Error: {field_name} must be a number. '{user_input}' isn't a number.")

def printNotStringError(field_name: str, user_input) -> None:
    print(f"Error: {field_name} must be a string. '{user_input}' isn't a string.")

def printShouldBeError(field_name: str, expected, actual) -> None:
    print(f"Error: {field_name} should be {expected} but got {actual}.")