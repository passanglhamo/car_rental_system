import re
from datetime import datetime, date

"""
    Methid to prompt the user to enter a valid email address.

    The function repeatedly prompts the user until an email
    address matching the expected format is provided.

    Returns:
        str: A validated email address.
    
"""
def get_valid_email():

    while True:
        email = input("Enter your email: ").strip()

        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        if re.match(pattern, email):
            return email

        print("Invalid email address. Please enter a valid email.")

"""
    Method to prompt the user to enter a valid password.

    The password must contain at least 8 characters, including
    at least one uppercase letter, one lowercase letter,
    one number, and one special character.

    Returns:
        str: A validated password.
    """
def get_valid_password():
   

    while True:
        password = input("Enter the password: ")

        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            continue

        if not re.search(r"[A-Z]", password):
            print("Password must contain at least one uppercase letter.")
            continue

        if not re.search(r"[a-z]", password):
            print("Password must contain at least one lowercase letter.")
            continue

        if not re.search(r"\d", password):
            print("Password must contain at least one number.")
            continue

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\]", password):
            print("Password must contain at least one special character.")
            continue

        return password        
"""
 Methdot to valid future date from the user. 
 The function repeatedly asks the user to enter a date in DD-MM-YYYY format.
 It validates the date format and ensures that the entered date is after today's date. 
 Args: prompt (str): Message displayed when requesting the date. 
 Returns: date: A valid future date entered by the user. """

def get_valid_date(prompt):
    while True:
        date_input = input(prompt).strip()

        try:
            entered_date = datetime.strptime(
                date_input, "%d-%m-%Y"
            ).date()

            if entered_date <= date.today():
                print("Please enter a future date.")
                continue

            return entered_date

        except ValueError:
            print("Invalid date. Please use DD-MM-YYYY format.")   