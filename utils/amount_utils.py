def format_currency(amount, symbol="$", decimals=2, default="N/A"):
    if amount is None:
        return default
    return f"{symbol}{amount:.{decimals}f}"