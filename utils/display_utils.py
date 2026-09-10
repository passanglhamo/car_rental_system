from utils.date_utils import format_date
from utils.amount_utils import format_currency
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

def display_booking_list(bookings, title, car_service):
    TABLE_WIDTH = 115  

    print("\n" + "=" * TABLE_WIDTH)
    print(f"{'🚗 ' + title:^{TABLE_WIDTH}}")
    print("=" * TABLE_WIDTH)

    if not bookings:
        print("No bookings found.")
        print("=" * TABLE_WIDTH)
        return

    print(f"{'#':<4}{'Car':<20}{'Start Date':<15}{'End Date':<15}"
          f"{'Pickup Date':<15}{'Return Date':<15}{'Fee':<12}{'Status':<12}")
    print("-" * TABLE_WIDTH)

    for idx, booking in enumerate(bookings, start=1):
        car = car_service.get_car_by_id(booking.car_id)
        car_label = f"{car.make} {car.model}"
        start_str = format_date(booking.start_date)
        end_str = format_date(booking.end_date)
        pick_str = format_date(booking.pick_up_date)
        return_str = format_date(booking.return_date)
        status = booking.status.value if hasattr(booking.status, "value") else booking.status

        print(f"{idx:<4}{car_label:<20}{start_str:<15}{end_str:<15}"
              f"{pick_str:<15}{return_str:<15}"
              f"{format_currency(booking.rental_fee):<12}{status:<12}")

    print("=" * TABLE_WIDTH)

def display_acc_creation_success(name,email):
    print("\n" + "=" * 50)
    print(f"{'✅  ACCOUNT CREATED SUCCESSFULLY':^50}")
    print("=" * 50)
    print(f"  Welcome, {name}!")
    print(f"  Email: {email}")
    print("=" * 50)  

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
