from datetime import datetime
"""
    Method to prompt the user to enter a valid date.

    The function repeatedly asks for a date until the user
    provides a valid date in DD-MM-YYYY format.

    Args:
        prompt: Message displayed when requesting the date.

    Returns:
        date: A Python date object representing the valid date.
"""
def get_valid_date(prompt):
    while True:
        date_input = input(prompt).strip()
        try:
            return datetime.strptime(date_input, "%d-%m-%Y").date()
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY (e.g. 15-08-2026).")
            
"""
    Method to format a date value into a user-friendly display format.

    The function accepts a date object or a string in either
    YYYY-MM-DD or DD-MM-YYYY format. The resulting date is
    displayed in DD Mon YYYY format.

    Args:
        value: Date object or date string to be formatted.
        default: Value returned when the input is None.

    Returns:
        str: Formatted date in DD Mon YYYY format.
             Returns the original value if a string cannot be parsed.
"""
def format_date(value, default=""):
    if value is None:
        return default
    if isinstance(value, str):
        for fmt in ('%Y-%m-%d', '%d-%m-%Y'):
            try:
                value = datetime.strptime(value, fmt).date()
                break
            except ValueError:
                continue
        else:
            return value
    return value.strftime('%d %b %Y')        