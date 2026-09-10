import sqlite3
from utils.password_utils import hash_password
from models.enums import role,status
import uuid
from datetime import date

admin_password = hash_password("a@dminRent#")

def create_connection():
    conn = sqlite3.connect("car_rental_system.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    

    # This table contain user information.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id      TEXT NOT NULL PRIMARY KEY,
            name    TEXT NOT NULL,
            email   TEXT NOT NULL UNIQUE,
            phone   TEXT NOT NULL,
            password TEXT NOT NULL,
            role    TEXT  NOT NULL,
            status  TEXT  NOT NULL,
            loyal_point  INTEGER,
            created_by TEXT NOT NULL,
            created_date DATE NOT NULL,
            updated_by TEXT,
            updated_date DATE,

            FOREIGN KEY (created_by) REFERENCES user(id)
            FOREIGN KEY (updated_by) REFERENCES user(id)
        )
    ''')

    

    # This table contain car information.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS car (
                id          TEXT NOT NULL PRIMARY KEY,
                make        TEXT NOT NULL,
                model       TEXT NOT NULL,
                year        INTEGER NOT NULL,
                mileage     REAL NOT NULL CHECK (mileage >= 0),
                min_period  INTEGER  NOT NULL,
                max_period  INTEGER  NOT NULL,
                daily_rate  REAL NOT NULL CHECK (daily_rate > 0),
                status      TEXT  NOT NULL,
                created_by TEXT NOT NULL,
                created_date DATE NOT NULL,
                updated_by TEXT,
                updated_date DATE,

                FOREIGN KEY (created_by) REFERENCES user(id)
                FOREIGN KEY (updated_by) REFERENCES user(id)

        )
        ''')

    # This table contain booking information.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS booking (
                    id           TEXT NOT NULL PRIMARY KEY,
                    car_id       TEXT NOT NULL,
                    user_id      TEXT NOT NULL,
                    booking_no   TEXT NOT NULL,
                    start_date   DATE NOT NULL,
                    end_date     DATE NOT NULL,
                    pick_up_date DATE,
                    payment_date DATE,
                    return_date  DATE,
                    rental_fee   REAL NOT NULL,
                    settlement_fee REAL,
                    status       TEXT  NOT NULL,
                    created_by TEXT NOT NULL,
                    created_date DATE NOT NULL,
                    updated_by TEXT,
                    updated_date DATE,
                                    
                    FOREIGN KEY (created_by) REFERENCES user(id)
                    FOREIGN KEY (updated_by) REFERENCES user(id)

                    FOREIGN KEY (car_id) REFERENCES car(id),
                    FOREIGN KEY (user_id) REFERENCES user(id)
    
         )
        ''')

    conn.commit()
    conn.close()
    print("All tables created successfully.")

def insert_data():
    conn = create_connection()
    cursor = conn.cursor()
    # Create default admin
    cursor.execute(
        "SELECT id FROM user WHERE email = ?",
        ("admin@rent.com",)
    )

    existing_admin = cursor.fetchone()

    if existing_admin is None:
        id=str(uuid.uuid4())
        cursor.execute('''
            INSERT INTO user (
                id,name, email, phone, password, role, status,created_by,created_date
            )
            VALUES (?, ?, ?, ?, ?, ?, ?,?,?)
        ''', (
            id,
            "System Administrator",
            "admin@rent.com",
            "0000000000",
            admin_password,
            role.SYSTEM_ADMIN.value,
            status.ACTIVE.value,
            id,
            date.today()

        ))

    conn.commit()
    conn.close()
    print("All data added successfully.")

def delete_admin():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM booking"
    )

    conn.commit()
    conn.close()

    print("Admin deleted successfully.")
