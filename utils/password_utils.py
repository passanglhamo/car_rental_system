import bcrypt

"""
    Method to securely hash a user's password using bcrypt.

    A random salt is generated automatically by bcrypt before
    hashing the password. The resulting hash can be stored in
    the database instead of storing the original password.

    Args:
        password: Plain-text password provided by the user.

    Returns:
        str: The bcrypt password hash encoded as a string.
"""
def hash_password(password):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

"""
    Method to verify a plain-text password against a stored bcrypt hash.

    Args:
        password: Plain-text password entered by the user.
        hashed_password: Previously generated bcrypt password hash.

    Returns:
        bool: True if the password matches the stored hash;
              otherwise, False.
"""
def verify_password(password, hashed_password):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )