import uuid

from models.Booking import Booking
from models.enums import role,booking_status
from utils.display_utils import display_booking_success_msg
from services.LoyaltyService import LoyaltyService
from services.SettlementService import SettlementService
from datetime import date,datetime
"""
    This service is class responsible for managing car rental bookings.

    It also uses LoyaltyService to calculate loyalty points and
    SettlementService to calculate late-return settlement fees.
"""
class BookingService:
    def __init__(self, car_repository,booking_repository,user_repository):
        self.booking_repository = booking_repository
        self.car_repository = car_repository
        self.user_repository = user_repository

        self.loyalty_service = LoyaltyService()
        self.settlement_service = SettlementService()
    """
        Method to create a new car rental booking.

        A new Booking object is created and saved when all validations
        are successful.

        Args:
            requesting_user (User): Customer making the booking.
            car (Car): Car selected for rental.
            start_date (date): Rental start date.
            end_date (date): Rental end date.
            rental_fee (float): Calculated rental fee.

        Returns:
            Booking, str, or None:
                Returns the saved booking if successful. Returns an
                error message or None when validation fails.
        """
    def book_car(self, requesting_user, car, start_date, end_date, rental_fee):
        if requesting_user is None:
            return "User is required."
        
        if requesting_user is None or not requesting_user.role == role.CUSTOMER.value:
            print("Only a Customer can book a car.")
            return None
        
        car = self.car_repository.find_by_id(car.id)
        if car is None:
            print("No car found.")
            return None
    

        if start_date is None:
            return "Start date is required."

        if end_date is None:
            return "End date is required."

        if start_date < date.today():
            return "Start date cannot be in the past."

        if end_date <= start_date:
            return "End date must be after start date."

        if self.booking_repository.has_booking(
            car.id,
            start_date,
            end_date
            ):
            print("\n========================================")
            print("       CAR IS ALREADY BOOKED")
            print("========================================")
            print("This car is already booked for the")
            print("selected rental period.")
            print("Please choose another date or car.")
            return
            
        booking = Booking(
        id=str(uuid.uuid4()),
        car_id=car.id,
        user_id=requesting_user.id,
        booking_no=self.booking_repository.generate_booking_number(),
        start_date=start_date,
        end_date=end_date,
        pick_up_date=None,
        payment_date=None,
        return_date=None,
        rental_fee=rental_fee,
        status=booking_status.PENDING.value,
        created_by=requesting_user.id,
        created_date=date.today()
        )

        bookingDetails = self.booking_repository.save(booking,requesting_user)
        display_booking_success_msg(bookingDetails)
        return bookingDetails
    """
        Update the status of an existing booking.

        Args:
            requesting_user (User): User performing the update.
            booking_id (str): ID of the booking to update.
            status: New booking status.

        Returns:
            Booking or None:Updated booking if successful, otherwise None.
    """
    def update_booking_status(self, requesting_user, booking_id,status):
        
        booking = self.booking_repository.update_status(booking_id, status,requesting_user.id)
        if booking is None:
            print("Booking not found.")
            return None
        return booking
    
    """
        Method to update the payment date and pick-up date of a booking.

        Only users with the Admin role are allowed to perform this
        operation.

        Args:
            requesting_user (User): Admin performing the update.
            booking_no (str): Booking number.
            payment_date (date): Date on which payment was made.
            pick_up_date (date): Date on which the car is picked up.

        Returns:
            None: Prints a success message or an error message.
        
    """
    def update_payment_pick_date(self, requesting_user, booking_no,payment_date,pick_up_date):
            if requesting_user is None or not requesting_user.role == role.ADMIN.value:
                print("Only an Admin can approve bookings.")
                return None
    
            booking = self.booking_repository.update_payment_pick_date(booking_no, payment_date,pick_up_date,requesting_user.id)
            if booking is None:
                print("Booking not found.")
                return None

            return print(f"Payment date and pick up date updated successfully.")
    
    """
        Method to retrieve bookings with a specified status.

        Args:
            requesting_user (User): Admin requesting the booking list.
            status: Booking status used as the search criterion.

        Returns:
            list: List of bookings matching the specified status.
    """
    def get_list_by_status(self,requesting_user,status):
        if requesting_user is None or not requesting_user.role == role.ADMIN.value:
            print("Only an Admin can view pending bookings.")
            return []

        list = self.booking_repository.find_by_status(status)
        if not list:
            print("No pending bookings.")

        return list
    """
        Method to retrieve bookings belonging to the requesting user with
        a specified booking status.

        Args:
            requesting_user (User): User whose bookings are requested.
            status: Booking status used to filter the results.

        Returns:
            list: List of matching bookings.
    """
    def get_list_by_status_user(self,requesting_user,status):
           
            list = self.booking_repository.find_by_status_user_id(status,requesting_user.id)
            if not list:
                print("No pending bookings.")
    
            return list
    """
        Method to retrieve all bookings belonging to the requesting user.

        Args:
            requesting_user (User): User whose bookings are requested.

        Returns:
            list: List of bookings belonging to the user.
    """
    def get_list_by_user_id(self,requesting_user):
            list = self.booking_repository.find_by_user_id(requesting_user.id)
            if not list:
                print("No pending bookings.")
            return list
    """
        Method to retrieve a booking using its booking number.

        Args:
            booking_no (str): Unique booking number.

        Returns:
            Booking or None: Matching booking if found.
    """
    def get_by_booking_no(self, booking_no):
        return self.booking_repository.find_by_booking_no(booking_no)
    
    """
        Method to record the return of a rented car.

        The method determines whether the car was returned on time
        or late. For on-time returns, loyalty points are calculated.
        For late returns, a settlement fee is calculated instead.

        An administrator must confirm the operation before the return
        is permanently recorded.

        Args:
            requesting_user (User): Admin recording the car return.
            booking (Booking): Booking associated with the returned car.
            return_date (date): Actual date the car was returned.

        Returns:
            Booking or None:
                Updated booking if the return was successfully recorded;
                otherwise None.
    """
    def record_return(self, requesting_user, booking, return_date):
        
     if requesting_user is None or requesting_user.role != role.ADMIN.value:
        print("Only an Admin can record a return.")
        return None

     loyalty_points = 0
     settlement_fee = 0
     end_date = (
        datetime.strptime(booking.end_date, "%Y-%m-%d").date()
        if isinstance(booking.end_date, str)
        else booking.end_date
)

     if return_date <= end_date:

        loyalty_points = self.loyalty_service.calculate_points(
            booking.rental_fee
        )

        print("\n=========== Return Calculation ===========")
        print("Return status    : On time")
        print(f"Rental fee       : ${booking.rental_fee:.2f}")
        print(f"Loyalty points   : {loyalty_points}")
        print("Settlement fee   : $0.00")

     else:

        late_days = self.settlement_service.calculate_late_days(
            booking.end_date,
            return_date
        )

        settlement_fee = self.settlement_service.calculate_settlement_fee(
            booking.end_date,
            return_date
        )

        print("\n=========== Return Calculation ===========")
        print("Return status    : Late")
        print(f"Expected return  : {booking.end_date}")
        print(f"Actual return    : {return_date}")
        print(f"Late days        : {late_days}")
        print(f"Settlement fee   : ${settlement_fee:.2f}")
        print("Loyalty points   : 0")

     while True:
        confirmation = input(
            "\nDo you want to continue with this return? (Y/N): "
        ).strip().lower()

        if confirmation == "y":
            break

        if confirmation == "n":
            print("Return operation cancelled.")
            return None

        print("Please enter Y or N.")
        

     updated_booking = self.booking_repository.record_return(
        booking.booking_no,
        return_date,
        settlement_fee,
        requesting_user.id,
        booking_status.RETURNED.value
     )

     if updated_booking is None:
        print("Failed to record return.")
        return None

     self.user_repository.update_loyal_point(
             loyalty_points,
             booking.user_id
          )

     print("\nReturn recorded successfully.")

     if loyalty_points > 0:
        print(f"Customer earned {loyalty_points} loyalty points.")

     if settlement_fee > 0:
        print(f"Settlement fee: {settlement_fee}")

        return updated_booking 

    