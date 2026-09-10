from models.User import User
from models.enums import role as Role, status as Status
import uuid
from datetime import date
class UserRepository:
    def __init__(self, db):
        self.db = db

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

    def email_exists(self, email):
        return self.find_by_email(email) is not None

    def find_by_email(self, email):
        return self._find_one("email", email)

    def find_by_id(self, user_id):
        return self._find_one("id", user_id)

    def find_all_by_role(self, role_value):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT id, name, email, password, phone, role, status,created_by,created_date "
            "FROM user WHERE role = ?",
            (str(role_value),),
        )
        return [self._row_to_user(row) for row in cursor.fetchall()]

    def _find_one(self, column, value):
        cursor = self.db.cursor()
        cursor.execute(
            f"SELECT id, name, email, password, phone, role,loyal_point,status,created_by,created_date "
            f"FROM user WHERE {column} = ?",
            (value,),
        )
        return self._row_to_user(cursor.fetchone())

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