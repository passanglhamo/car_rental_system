from models.Car import Car
import sqlite3
from datetime import date


class CarRepository:
    def __init__(self, db: sqlite3.Connection):
        self.db = db

    """Method to get all cars"""
    def find_all(self):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT id, make, model, year, " \
            "mileage, min_period, max_period, daily_rate,created_by,created_date FROM car"
        )
        rows = cursor.fetchall()
        return [self._row_to_car(row) for row in rows]

    """Method to get latest cars as per limit"""
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

    """Method to get latest car by id"""
    def find_by_id(self, car_id):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT id, make, model, year, mileage, min_period, max_period, daily_rate,created_by,created_date "
            "FROM car WHERE id = ?",
            (car_id,)
        )
        row = cursor.fetchone()
        return self._row_to_car(row) if row else None
    
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