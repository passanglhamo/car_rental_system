from utils.date_utils import format_date
from utils.amount_utils import format_currency
"""
    Method to display a list of available cars in a formatted table.

    Args:
        cars: List of car objects to display.
        title: Heading displayed above the car list.

    Returns:
        None
"""
def display_car_list(cars, title):
    print("\n" + "=" * 75)
    print(f"{'🚗'+" "+title:^70}")
    print("=" * 75)

    if not cars:
        print("No cars available at the moment.")
        print("=" * 75)
        return

    print(f"{'#':<4}{'Make':<12}{'Model':<14}{'Year':<8}{'Price/Day':<12}{'Min Period':<12}{'Max Period':<12}")
    print("-" * 75)

    for idx, car in enumerate(cars, start=1):
        print(f"{idx:<4}{car.make:<12}{car.model:<14}{car.year:<8}"
              f"${car.daily_rate:<11.2f}{car.min_period:<12}{car.max_period:<12}")

    print("=" * 75)  

"""
    Method to display a list of users in a formatted table.

    Args:
        users: List of user objects to display.
        title: Heading displayed above the user list.

    Returns:
        None
"""
def display_user_list(users, title):
    print("\n" + "=" * 75)
    print(f"{'🚗'+" "+title:^70}")
    print("=" * 75)

    if not users:
        print("No users available at the moment.")
        print("=" * 75)
        return

    print(f"{'#':<4}{'Name':<12}{'Email':<15}{'Phone':<15}{'Status':<12}")
    print("-" * 75)

    for idx, user in enumerate(users, start=1):
        print(f"{idx:<4}{user.name:<12}{user.email:<15}{user.phone:<15}"
              f"{user.status:<12}")

    print("=" * 75)  
    
"""
    Method to display a successful account creation message.

    Args:
        name: Name of the newly registered user.
        email: Email address of the newly registered user.

    Returns:
        None
    
"""
def display_booking_list(bookings, title, car_service):
    TABLE_WIDTH = 125  

    print("\n" + "=" * TABLE_WIDTH)
    print(f"{'🚗 ' + title:^{TABLE_WIDTH}}")
    print("=" * TABLE_WIDTH)

    if not bookings:
        print("No bookings found.")
        print("=" * TABLE_WIDTH)
        return

    print(f"{'#':<4}{'Booking #':<20}{'Car':<20}{'Start Date':<15}{'End Date':<15}"
          f"{'Pickup Date':<15}{'Return Date':<15}{'Fee':<12}{'Status':<12}")
    print("-" * TABLE_WIDTH)

    for idx, booking in enumerate(bookings, start=1):
        car = car_service.get_car_by_id(booking.car_id)
        booking_no = f"{booking.booking_no}"
        car_label = f"{car.make} {car.model}"
        start_str = format_date(booking.start_date)
        end_str = format_date(booking.end_date)
        pick_str = format_date(booking.pick_up_date)
        return_str = format_date(booking.return_date)
        status = booking.status.value if hasattr(booking.status, "value") else booking.status

        print(f"{idx:<4}{booking_no:<20}{car_label:<20}{start_str:<15}{end_str:<15}"
              f"{pick_str:<15}{return_str:<15}"
              f"{format_currency(booking.rental_fee):<12}{status:<12}")

    print("=" * TABLE_WIDTH)
    
"""
    Method to display a short summary line for any list of entities that
    subclass BaseEntity (User, Car, Booking, or a mix of them).

    Demonstrates polymorphism: the same summary() call produces a
    different, type-specific line depending on the actual object type.

    Args:
        entities: List of BaseEntity subclass instances to display.
        title: Heading displayed above the list.

    Returns:
        None
"""
def display_entity_summaries(entities, title="OVERVIEW"):
    print("\n" + "=" * 75)
    print(f"{title:^75}")
    print("=" * 75)

    if not entities:
        print("Nothing to display.")
        print("=" * 75)
        return

    for idx, entity in enumerate(entities, start=1):
        print(f"{idx:<4}{entity.summary()}")

    print("=" * 75)    
    
"""
    Method to display a successful account creation message.

    Args:
        name: Name of the newly registered user.
        email: Email address of the newly registered user.

    Returns:
        None
    
"""
def display_acc_creation_success(name,email):
    print("\n" + "=" * 50)
    print(f"{'✅  ACCOUNT CREATED SUCCESSFULLY':^50}")
    print("=" * 50)
    print(f"  Welcome, {name}!")
    print(f"  Email: {email}")
    print("=" * 50)  
"""
    Method to display a confirmation message after a booking request
    has been successfully submitted.

    Args:
        bookingDetails: Booking object containing the booking
                        number, dates, rental fee, and status.

    Returns:
        None
    
"""
def display_booking_success_msg(bookingDetails):
    print("\n")
    print("=" * 65)
    print("                 BOOKING REQUEST SUBMITTED")
    print("=" * 65)
    print()
    print("  Your booking request has been submitted successfully!")
    print()
    print(f"  Booking Number : {bookingDetails.booking_no}")
    print(f"  Start Date     : {format_date(bookingDetails.start_date)}")
    print(f"  End Date       : {format_date(bookingDetails.end_date)}")
    print(f"  Pick-up Date   : {format_date(bookingDetails.pick_up_date)}")
    print(f"  Rental Fee     : ${bookingDetails.rental_fee:.2f}")
    print(f"  Status         : {bookingDetails.status}")
    print()
    print("  Your booking is waiting for Admin approval.")
    print("  Once approved, please come to pick up the car and settle")
    print("  the amount at that time.")
    print()
    print("=" * 65)
    print()          
