
from models.Booking import Booking

from datetime import datetime,date

class BookingRepository:

    def __init__(self, db):
        self.db = db
        

    def save(self, booking: Booking,user):

        cursor = self.db.cursor()

        cursor.execute(
    """
    INSERT INTO booking (
        id,
        car_id,
        user_id,
        booking_no,
        start_date,
        end_date,
        rental_fee,
        status,
        created_by,
        created_date,
        updated_by,
        updated_date
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        booking.id,
        booking.car_id,
        booking.user_id,
        booking.booking_no,
        booking.start_date,
        booking.end_date,
        booking.rental_fee,
        booking.status,
        user.id,          
        date.today(),     
        None,             
        None              
        )
        )

        self.db.commit()

        return booking

    def update_status(self, booking_id, status, user_id):

        cursor = self.db.cursor()

        cursor.execute(
        """
        UPDATE booking
        SET status = ?,
            updated_by = ?,
            updated_date = ?
        WHERE id = ?
        """,
        (
            status.value if hasattr(status, "value") else status,
            user_id,
            date.today(),
            booking_id
        )
        )

        self.db.commit()

        return self.find_by_id(booking_id)

    def update_payment_pick_date(self, booking_no, payment_date,pick_up_date,user_id):
        cursor = self.db.cursor()

        cursor.execute(
            """
            UPDATE booking
            SET payment_date = ?,
            pick_up_date=?,
            updated_by = ?,
            updated_date = ?
            WHERE booking_no = ?
            """,
            (payment_date,pick_up_date,user_id,date.today(),booking_no)
        )

        self.db.commit()

        return self.find_by_booking_no(booking_no)

    def record_return(self, booking_no, return_date,settlement_fee,user_id):
            cursor = self.db.cursor()
    
            cursor.execute(
                """
                UPDATE booking
                SET return_date = ?,
                settlement_fee=?,
                updated_by = ?,
                updated_date = ?
                WHERE booking_no = ?
                """,
                (return_date,settlement_fee, user_id,date.today(),booking_no)
            )
    
            self.db.commit()
    
            return self.find_by_booking_no(booking_no)

    def find_by_id(self, booking_id):

        cursor = self.db.cursor()

        cursor.execute(
        """
        SELECT id, car_id, user_id,booking_no,start_date,end_date,pick_up_date,
                    payment_date,return_date,rental_fee,status,created_by,created_date
        FROM booking
        WHERE id = ?
        """,
        (booking_id,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return self._row_to_booking(row)

    def find_by_status(self, status):
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT id, car_id, user_id,booking_no,start_date,end_date,pick_up_date,
            payment_date,return_date,rental_fee,status,created_by,created_date
            FROM booking WHERE status = ?
            """,
            (str(status),),
        )
        rows = cursor.fetchall()
        return [self._row_to_booking(row) for row in rows]

    def find_by_booking_no(self, booking_no):
    
            cursor = self.db.cursor()
    
            cursor.execute(
            """
            SELECT id, car_id, user_id, booking_no,
                   start_date, end_date, pick_up_date,payment_date,return_date,
                   rental_fee,status,created_by,created_date 
            FROM booking
            WHERE booking_no = ?
            """,
            (booking_no,)
            )
    
            row = cursor.fetchone()
    
            if row is None:
                return None
    
            return self._row_to_booking(row)

    def find_by_user_id(self, user_id):
            cursor = self.db.cursor()
            cursor.execute(
                """SELECT id, car_id, user_id,booking_no,start_date,end_date,pick_up_date,
                payment_date,return_date,rental_fee, status,created_by,created_date 
                FROM booking WHERE user_id = ?
                """,
                (user_id,),
            )
            rows = cursor.fetchall()
            return [self._row_to_booking(row) for row in rows]
    
    def find_by_status_user_id(self, status,user_id):
                cursor = self.db.cursor()
                cursor.execute(
                    """SELECT id, car_id, user_id,booking_no,start_date,end_date,pick_up_date,
                    payment_date,return_date,rental_fee, status,created_by,created_date 
                    FROM booking WHERE user_id = ? AND status = ?
                    """,
                    (user_id,status,),
                )
                rows = cursor.fetchall()
                return [self._row_to_booking(row) for row in rows]

    def generate_booking_number(self):

        today = datetime.now().strftime("%d%m%y")

        cursor = self.db.cursor()

        cursor.execute(
            """
            SELECT booking_no
            FROM booking
            WHERE booking_no LIKE ?
            ORDER BY booking_no DESC
            LIMIT 1
            """,
            (f"B{today}-%",)
        )

        result = cursor.fetchone()

        if result:
            last_number = int(result[0].split("-")[1])
            next_number = last_number + 1
        else:
            next_number = 1

        return f"B{today}-{next_number:05d}"    

    def has_booking(self, car_id, start_date, end_date):
        cursor = self.db.cursor()

        cursor.execute("""
        SELECT 1
        FROM booking
        WHERE car_id = ?
          AND status IN ('PENDING', 'APPROVED')
          AND start_date < ?
          AND end_date > ?
        LIMIT 1
        """, (
        car_id,
        end_date,
        start_date
        ))

        return cursor.fetchone() is not None

    @staticmethod
    def _row_to_booking(row) -> Booking:
        return Booking(
        id=row[0],
        car_id=row[1],
        user_id=row[2],
        booking_no=row[3],
        start_date=row[4],
        end_date=row[5],
        pick_up_date=row[6],
        payment_date=row[7],
        return_date=row[8],
        rental_fee=row[9],
        status=row[10],
        created_by=row[11],
        created_date=row[12]
        )    