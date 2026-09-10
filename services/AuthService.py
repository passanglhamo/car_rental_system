from utils.password_utils import verify_password

class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service

    def login(self, username, password):
        user = self.user_service.find_by_email(username)
        if user and verify_password(password, user._password):
            return user
        return None