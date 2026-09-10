from datetime import datetime

def get_valid_date(prompt):
    while True:
        date_input = input(prompt).strip()
        try:
            return datetime.strptime(date_input, "%d-%m-%Y").date()
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY (e.g. 15-08-2026).")

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