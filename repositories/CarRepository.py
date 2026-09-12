from models.Car import Car
import sqlite3
from datetime import date
"""
This module provides database operations for the Car entity.

The CarRepository class is responsible for creating, retrieving,
and updating car records in the car rental system. It also provides
functionality to find available cars based on a requested rental period.
"""

class CarRepository:
    def __init__(self, db: sqlite3.Connection):
        self.db = db


    """
        Method to get all cars from the database.

        Returns:
            list[Car]: A list containing all car records.
    """
    def find_all(self):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT id, make, model, year, " \
            "mileage, min_period, max_period, daily_rate,created_by,created_date FROM car"
        )
        rows = cursor.fetchall()
        return [self._row_to_car(row) for row in rows]

    """
        Method to get the latest cars up to the specified limit.

        Args:
            limit (int): Maximum number of cars to return.
                Defaults to 5.

        Returns:
            list[Car]: A list of the latest car records.
    """
    def find_by_limit(self, limit=5):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT id, make, model, year, mileage, "
            "min_period, max_period, daily_rate,created_by,created_date FROM car "
            "ORDER BY id DESC LIMIT ?",
            (limit,)
        )
        rows = cursor.fetchall()
        return [self._row_to_car(row) for row in rows]
    """
        Method to get cars that are available during a specified rental period.

        Cars with existing PENDING or APPROVED bookings that overlap
        with the requested rental period are excluded.

        Args:
            start_date (date): Requested rental start date.
            end_date (date): Requested rental end date.

        Returns:
            list[Car]: List of cars available for the requested period.
    """
    def find_by_available(self, start_date, end_date):
        cursor = self.db.cursor()

        cursor.execute("""
        SELECT id, make, model, year, mileage,
               min_period, max_period, daily_rate,
               created_by, created_date
        FROM car
        WHERE id NOT IN (
            SELECT car_id
            FROM booking
            WHERE status IN ('pending', 'approved')
              AND start_date < ?
              AND end_date > ?
        )
        """, (end_date, start_date))

        rows = cursor.fetchall()

        return [self._row_to_car(row) for row in rows]

    """
        Method to get a car using its ID.

        Args:
            car_id (str): Unique identifier of the car.

        Returns:
            Car or None: The matching car if found; otherwise None.
    """
    def find_by_id(self, car_id):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT id, make, model, year, mileage, min_period, max_period, daily_rate,created_by,created_date "
            "FROM car WHERE id = ?",
            (car_id,)
        )
        row = cursor.fetchone()
        return self._row_to_car(row) if row else None
    
    """
        Method to save a car record to the database.

        Args:
            car (Car): Car object containing the details.
            user_id (str): ID of the user creating the car record.

        Returns:
            Car: The saved car object.
    """   
    def save(self, car: Car,user_id):
        cursor = self.db.cursor()
        cursor.execute(
            """INSERT INTO car (id, make, model, year, mileage, 
            min_period, max_period,
            daily_rate,status,created_by,
            created_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)
            """,
            (car.id, car.make, car.model, car.year, car.mileage,
             car.min_period, car.max_period, car.daily_rate,car.status,
             user_id,date.today())
        )
        self.db.commit()
        return car
    """
        Method to update an existing car record.

        Args:
            car_id (str): ID of the car to update.
            updated_car (Car): Car object containing the updated details.
            user_id (str): ID of the user performing the update.

        Returns:
            Car: Updated car object.
    """
    def update(self, car_id, updated_car: Car,user_id):
        cursor = self.db.cursor()
        cursor.execute(
            "UPDATE car SET make=?, model=?, year=?, mileage=?, "
            "min_period=?, max_period=?, daily_rate=?, updated_by = ?,updated_date = ? WHERE id=?",
            (updated_car.make, updated_car.model, updated_car.year, updated_car.mileage,
             updated_car.min_period, updated_car.max_period,
             updated_car.daily_rate,user_id,date.today(),car_id)
        )
        self.db.commit()
        return updated_car

    @staticmethod
    def _row_to_car(row) -> Car:
        return Car(
            id=row[0], 
            make=row[1], 
            model=row[2], 
            year=row[3],
            mileage=row[4], 
            min_period=row[5], 
            max_period=row[6], 
            daily_rate=row[7],
            created_by=row[8],
            created_date=row[9]

        )