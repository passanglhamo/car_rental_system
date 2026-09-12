from models.enums import status
from utils.password_utils import hash_password
from datetime import date
"""
    This service is responsible for managing user-related operations.

    UserService communicates with the UserRepository to retrieve,
    create, and update user information. It also handles business
    logic such as checking for duplicate email addresses and
    hashing passwords before storing them.
    
"""
class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository
    """
        Method to retrieve all users from the database.

        Returns:
            list: A list of all users.
    """
    def get_all_users(self):
        return self.user_repository.get_all_users()
    """
        Method to retrieve a user using their unique ID.

        Args:
            user_id: Unique identifier of the user.

        Returns:
            User: The user associated with the given ID.
    """
    def get_user_by_id(self, user_id):
        return self.user_repository.find_by_id(user_id)
    """
        Method to retrieve all users having a specific role.

        Args:
            role: Role used to filter the users.

        Returns:
            list: Users matching the specified role.
    """
    def get_users_by_role(self, role):
        return self.user_repository.find_all_by_role(role)
    """
        Method to retrieve a user using their email address.

        Args:
            email: Email address of the user.

        Returns:
            User: The user associated with the email address.
    """
    def get_user_by_email(self, email):
        return self.user_repository.find_by_email(email)
    """
        Method to save a new user to the database.

        A unique UUID is generated for the user. 
        Args:
            user (User): User object containing the information to save.

        Returns:
            User: The newly created user retrieved from the database.
    """
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
    """
        Method to update a existing user to the database.

        Args:
            updated_user (User): User object containing the information to update.
            user_id: Unique identifier of the user.

        Returns:
            User: The updated  user information retrieved from the database.
    """
    def update_user(self, user_id, updated_user,updated_by):
        return self.user_repository.update_user(user_id, updated_user,updated_by)
