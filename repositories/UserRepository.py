from models.User import User
from models.enums import role as Role, status as Status
import uuid
from datetime import date
"""
    This module provides database operations for the Booking entity.

    This class provides methods to create, retrieve, and update user
    information in the SQLite database.
"""
class UserRepository:
    def __init__(self, db):
        self.db = db
    """
        Method to save a new user to the database.

        A unique UUID is generated for the user. 
        Args:
            user (User): User object containing the information to save.

        Returns:
            User: The newly created user retrieved from the database.
    """
    def save(self, user):
        cursor = self.db.cursor()
        id=str(uuid.uuid4())
        cursor.execute(
            "INSERT INTO user (id, name, email, password, phone, role, status,created_by,created_date) "
            "VALUES (?, ?, ?, ?, ?, ?, ?,?,?)",
            (id, user.name, user.email, user.password,
             user.phone, str(user.role), str(user.status),
             user.created_by or id,user.created_date or date.today()),
        )
        self.db.commit()
        return self.find_by_email(user.email)

    """
        Method to add loyalty points to an existing user's loyalty point balance.

        The COALESCE function ensures that a NULL loyalty point value
        is treated as zero before adding the new points.

        Args:
            loyal_point (int): Number of loyalty points.
            user_id (str): Unique ID of the user.

        Returns:
            User: Updated user object after the loyalty points are added.
    """
    
    def update_loyal_point(self,loyal_point,user_id):
    
            cursor = self.db.cursor()
    
            cursor.execute(
            """
            UPDATE user
            SET loyal_point = COALESCE(loyal_point, 0) + ?,
                updated_by = ?,
                updated_date = ?
            WHERE id = ?
            """,
            (
               loyal_point,
               user_id,
               date.today(),
               user_id
            )
            )
    
            self.db.commit()
    
            return self.find_by_id(user_id)
    """
        Method to check whether a user with the specified email exists.

        Args:
            email (str): Email address to check.

        Returns:
            bool: True if the email exists; otherwise False.
    """
    def email_exists(self, email):
        return self.find_by_email(email) is not None
    
    """
        Method o find a user using their email address.

        Args:
            email (str): Email address of the user.

        Returns:
            User or None: Matching User object, or None if no user is found.
    """
    def find_by_email(self, email):
        return self._find_one("email", email)
    
    """
        method to find a user using their unique user ID.

        Args:
            user_id (str): Unique ID of the user.

        Returns:
            User or None: Matching User object, or None if no user is found.
    """
    def find_by_id(self, user_id):
        return self._find_one("id", user_id)
    
    """
        Method to retrieve all users that have a specified role.

        Args:
            role_value: Role value used to filter users.

        Returns:
            list[User]: List of User objects matching the specified role.
    """
    def find_all_by_role(self, role_value):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT id, name, email, password, phone, role,loyal_point,status,created_by,created_date "
            "FROM user WHERE role = ?",
            (str(role_value),),
        )
        return [self._row_to_user(row) for row in cursor.fetchall()]
    
    """
        Method to find a single user based on a specified database column.

        This is a private helper method used by methods such as
        find_by_id() and find_by_email() to avoid duplicating
        database query logic.

        Args:
            column (str): Database column used for searching.
            value: Value to search for.

        Returns:
            User or None: Matching User object, or None if no record exists.
        
    """
    def _find_one(self, column, value):
    
        cursor = self.db.cursor()
        cursor.execute(
            f"SELECT id, name, email, password, phone, role,loyal_point,status,created_by,created_date "
            f"FROM user WHERE {column} = ?",
            (value,),
        )
        return self._row_to_user(cursor.fetchone())
    
    """ Updates a user's name, phone number, and status in the database.
       The method also records who performed the update and the date on which the update was made.
        Args: user_id: The ID of the user being updated. 
        updated_user: The User object containing the updated information. 
        updated_by: The ID or identifier of the user who performed the update. 
        Returns: None 
    """
    def update_user(self, user_id, updated_user,updated_by):
        cursor = self.db.cursor()
        cursor.execute(
            """
            UPDATE user
            SET name = ?,
                phone = ?,
                status = ?,
                loyal_point=?,
                updated_by = ?,
                updated_date = ?
            WHERE id = ?
            """,
            (
               updated_user.name,
               updated_user.phone,
               updated_user.status,
               updated_user.loyal_point,
               updated_by,
               date.today(),
               user_id
            )
            )
    
        self.db.commit()
        return self.find_by_id(user_id)

 

    def _row_to_user(self, row):
        if row is None:
            return None

        return User(
            id=row[0],
            name=row[1],
            email=row[2],
            _password=row[3],
            phone=row[4],
            role=row[5],
            loyal_point=row[6],
            status=row[7],
            created_by=row[8],
            created_date=row[9]
        )