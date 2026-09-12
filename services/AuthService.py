from utils.password_utils import verify_password
"""
    This service class is responsible for user authentication.

    AuthService verifies a user's email and password by retrieving
    the user through UserService and validating the supplied password
    against the stored password.
"""
class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service
    """
        Method to authenticate a user using their email and password.

        The method first searches for a user using the supplied
        username/email. If the user exists, the supplied password
        is verified against the user's stored password.

        Args:
            username (str): User's email address.
            password (str): Password entered by the user.

        Returns:
            User or None:
                Returns the authenticated User object if the credentials
                are valid. Returns None if authentication fails.
    """
    def login(self, username, password):
        user = self.user_service.get_user_by_email(username)
        if user and user.check_password(password):
            return user
        return None