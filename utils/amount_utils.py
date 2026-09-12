"""
    Method to format a numeric amount as a currency value.

    Args:
        amount: The amount to be formatted. If None, the default
                value is returned.
        symbol: Currency symbol to display. Defaults to "$".
        decimals: Number of decimal places to display. Defaults to 2.
        default: Value returned when amount is None. Defaults to "N/A".

    Returns:
        str: The formatted currency value.

    Examples:
        format_currency(150) -> "$150.00"
        format_currency(99.5) -> "$99.50"
        format_currency(None) -> "N/A"
    """
def format_currency(amount, symbol="$", decimals=2, default="N/A"):
    if amount is None:
        return default
    return f"{symbol}{amount:.{decimals}f}"