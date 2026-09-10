from models.enums import role,booking_status
from utils.display_utils import display_car_list,display_booking_list
from utils.booking_utils import browse_and_book
from utils.date_utils import get_valid_date,format_date
from utils.amount_utils import format_currency

def system_admin_menu(user,user_service):
    while True:
        print("\nSystem Admin Menu:")
        print("1. Add a new admin")
        print("2. View all admins")
        print("3. Logout")
        choice = input("Select an option: ").strip()

        if choice == "1":
            print("=========== Add a new Admin ===========")
            name = input("Enter your full name: ").strip()
            email = input("Enter your email: ").strip()
            password = input("Enter the password: ").strip()
            phone = input("Enter your contact number: ").strip()
            new_admin = user_service.save(
                            user,
                            name,
                            email,
                            password,
                            phone,
                            role.ADMIN.value
                            )

            if new_admin:
                print("\n========================================")
                print("       Admin added successfully       ")
                print("========================================")
                print(f"Name  : {new_admin.name}")
                print(f"Email : {new_admin.email}")
                print(f"Phone : {new_admin.phone}")
            else:
                print("\nFailed to add admin.")

        elif choice == "2":
                print("=========== View All Admins ===========")
                users = user_service.get_users_by_role(role.ADMIN.value)
                if not users:
                    print(f"No users found with role: {role}")
                    return []

                print(f"{'Name':<20} {'Email':<25} {'Phone':<15} {'Status':<10}")
                print("-" * 106)
                for user in users:
                    print(f"{user.name:<20} {user.email:<25} {user.phone:<15} {str(user.status):<10}")

                print(f"\nTotal: {len(users)} admin(s)")
        elif choice == "3":
            print("You have been logged out.")
            user = None
            break
        else:
            print("Invalid option. Please try again.")

def admin_menu(user, car_service,booking_service):
    while True:
        print(f"\n--- Admin Menu ({user.name}) ---")
        print("1. View available cars")
        print("2. View all cars")
        print("3. Add a car")
        print("4. Update a car information")
        print("5. View pending booking requests")
        print("6. Approve a booking")
        print("7. Reject a booking")
        print("8. Update payment status")
        print("9. Add return information")
        print("10. Logout")
        choice = input("Select an option: ").strip()

        if choice == "1":

            start_date = get_valid_date(
                "Enter start date (DD-MM-YYYY): "
            )

            while True:
                end_date = get_valid_date(
                "Enter end date (DD-MM-YYYY): "
                )

                if end_date <= start_date:
                    print("End date must be after start date.")
                    continue

                break
            cars = car_service.find_by_available(start_date,end_date)
            display_car_list(cars,"Available Cars")
        elif choice == "2":
            cars = car_service.find_all()
            display_car_list(cars,"Cars List")

        elif choice == "3":
            print("=========== Add a new car ===========")
            car = car_service.save(user) 
            if car: 
                print("\n======================================") 
                print(" Car added successfully ") 
                print("======================================") 
                print(f"Car ID : {car.id}") 
                print(f"Make : {car.make}") 
                print(f"Model : {car.model}") 
                print(f"Year : {car.year}") 
                print(f"Daily Rate : ${car.daily_rate:.2f}") 
            else: 
                print("\nFailed to add car.")

        elif choice == "4":
            cars = car_service.find_all()
            display_car_list(cars, "All Cars")
            try:
                car_no = input("Enter the # of the car to update: ").strip()

                car_index = int(car_no) - 1

                if car_index < 0 or car_index >= len(cars):
                    print("Invalid car number.")
                else:
                    car_id = cars[car_index].id

                car = car_service.update_car(car_id,user)
                if car: 
                    print("\n======================================") 
                    print(" Car updated successfully ") 
                    print("======================================") 
                    print(f"Car ID : {car.id}") 
                    print(f"Make : {car.make}") 
                    print(f"Model : {car.model}") 
                    print(f"Year : {car.year}") 
                    print(f"Daily Rate : ${car.daily_rate:.2f}") 
                else: 
                    print("\nFailed to add car.")
                

            except ValueError:
                print("Please enter a valid car number.")
        elif choice == "5":
            print("=========== Pending Booking Requests ===========")
            booking =booking_service.get_list_by_status(user,booking_status.PENDING.value)
            display_booking_list(booking,"Pending Booking List",car_service)
        elif choice == "6":
            process_booking(
                user,
                booking_service,
                car_service,
                booking_status.APPROVED.value,
                "Approve"
                )
        elif choice == "7":
             process_booking(
                user,
                booking_service,
                car_service,
                booking_status.REJECTED.value,
                "Reject"
                )
        elif choice == "8":
            print("\n=========== Record Payment Date and Pick up date ===========")
            booking_no = input("Enter booking number: ").strip()
            if not booking_no:
                continue

            booking = booking_service.get_by_booking_no(booking_no)
            if booking is None:
                print("Booking not found.")
                continue
            if booking.status != booking_status.APPROVED.value:
                print("Payment and pick-up date can only be updated for approved bookings.")
                return None

            display_booking_details(booking)
            payment_date = get_valid_date(f"Enter the payment date (DD-MM-YYYY): ")
            pick_up_date = get_valid_date(f"Enter the pick up date (DD-MM-YYYY): ")

            try:
                booking_service.update_payment_pick_date(user,booking_no,payment_date,pick_up_date)
            except ValueError:
                print(f"Invalid date. Please use DD-MM-YYYY.") 

        elif choice == "9":
            print("\n=========== Record Return Information ===========")
            booking_no = input("Enter booking number: ").strip()
            if not booking_no:
                    continue
                
            booking = booking_service.get_by_booking_no(booking_no)
            if booking is None:
                print("Booking not found.")
                continue

            if booking.payment_date is None:
                print("Car cannot be returned because payment has not been completed.")
                continue
                
            display_booking_details(booking)
            return_date = get_valid_date(f"Enter the return date (DD-MM-YYYY): ")

            try:
                booking_service.record_return(user,booking,return_date)
            except ValueError:
                    print(f"Invalid date. Please use DD-MM-YYYY.")       
           
        elif choice == "10":
            print("You have been logged out.")
            user = None
            break
        else:
            print("Invalid option.\n")

def customer_menu(user, car_service,auth_service,user_service, booking_service):

    while True:
        print("\n" + "=" * 50)
        print("              CUSTOMER MENU")
        print("=" * 50)

        print(f"Welcome, {user.name}!")
        print()
        print("1. Browse Cars")
        print("2. My Bookings")
        print("3. Cancel Booking")
        print("4. Logout")

        print("=" * 50)

        choice = input("Select an option: ").strip()

        if choice == "1":
            browse_and_book(user,car_service,auth_service,user_service,booking_service)
        elif choice == "2":
            bookings = booking_service.get_list_by_user_id(user)
            display_booking_list(
                    bookings,
                    "My Bookings",
                    car_service
                )
        elif choice == "3":    
           process_booking(
                           user,
                           booking_service,
                           car_service,
                           booking_status.CANCELLED.value,
                           "Cancel"
                           )
        elif choice == "4":
            print("You have been logged out.")
            user = None
            return

        else:
            print("Invalid option. Please try again.")  


def process_booking(user, booking_service, car_service, new_status, action_name):

    print(f"\n=========== {action_name} Booking ===========")

    if new_status == booking_status.CANCELLED.value:
        bookings = booking_service.get_list_by_status_user(
                    user,
                    booking_status.PENDING.value
                )
    else:

        bookings = booking_service.get_list_by_status(
            user,
            booking_status.PENDING.value
        )

    if not bookings:
        print("No pending booking requests.")
        return

    display_booking_list(
        bookings,
        "Pending Booking Requests",
        car_service
    )

    selection = input(
        f"\nEnter the # of the booking to {action_name.lower()}, "
        "or press Enter to go back: "
    ).strip()

    if not selection:
        return

    try:
        selected_index = int(selection) - 1

        if selected_index < 0 or selected_index >= len(bookings):
            print("Invalid booking selection.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    selected_booking = bookings[selected_index]

    print("\nSelected Booking")
    print(f"Booking Number : {selected_booking.booking_no}")
    print(f"Status         : {selected_booking.status}")

    confirm = input(
        f"\n{action_name} this booking? (Y/N): "
    ).strip().lower()

    if confirm != "y":
        print(f"\nBooking {action_name.lower()} cancelled.")
        return

    booking_service.update_booking_status(
        user,
        selected_booking.id,
        new_status
    )

    print(
        f"\nBooking {selected_booking.booking_no} "
        f"has been {action_name.lower()}d successfully."
    )

def display_booking_details(booking):
    print("\nBooking Details")
    print("-" * 40)
    print(f"Booking Number : {booking.booking_no}")
    print(f"Start Date     : {format_date(booking.start_date)}")
    print(f"End Date       : {format_date(booking.end_date)}")
    print(f"Rental Fee     : {format_currency(booking.rental_fee)}")
    print(f"Status         : {booking.status}")
    print(f"Payment Date   : {format_date(booking.payment_date)}")
    print(f"Return Date    : {format_date(booking.return_date)}")
    print("-" * 40)


      