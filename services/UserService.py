from models.enums import status
from utils.password_utils import hash_password
from datetime import date

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def get_users_by_role(self, role):
        return self.user_repository.find_all_by_role(role)

    def find_by_email(self, email):
        return self.user_repository.find_by_email(email)

    def save(self,user, name,email,password,phone,role):
        if self.user_repository.email_exists(email):
            print("The user with the email "+email+" already exists.")
            return None
        
        hashed_password = hash_password(password)
        user = type('User', (object,), {
            'name': name,
            'email': email, 
            'password': hashed_password,
            'phone':phone, 
            'role': role,
            'status': status.ACTIVE.value,
            'created_by': user.id if user is not None else None,
            'created_date': date.today(),
            'updated_by': None,
            'updated_date': None})()
        

        return self.user_repository.save(user)

    def update_user(self, user_id, updated_user):
        return self.user_repository.update_user(user_id, updated_user)
