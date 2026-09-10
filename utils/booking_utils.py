from utils.display_utils import display_car_list,display_acc_creation_success
from models.enums import role
from utils.date_utils import get_valid_date

def browse_and_book(user,car_service,auth_service,user_service,booking_service):
    print("\n=== Browse Available Cars ===")
    cars = car_service.find_all()

    if not cars:
        print("No cars currently available.")
        return

    print("1. View all cars")
    print("2. Search/filter cars")
    choice = input("Select an option: ").strip()

    if choice == "2":
        cars = apply_search_filters(cars)
        title = "Search Results"
    else:
        title = "All Available Cars"

    if not cars:
        print("No cars match your search criteria.")
        return

    display_car_list(cars, title=title)

    selection = input("\nEnter the # to book that car, or press Enter to go back: ").strip()

    if not selection:
        return

    try:
        selected_idx = int(selection) - 1
        if selected_idx < 0 or selected_idx >= len(cars):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid input — please enter a number.")
        return

    selected_car = cars[selected_idx]
    if user is None:
        print("\nYou need an account to book a car.")
        print("1. Login")
        print("2. Sign up (Customer)")
        print("3. Cancel")
        auth_choice = input("Select an option: ").strip()

        if auth_choice == "1":
            user = login(auth_service)
        elif auth_choice == "2":
            user = signup_customer(user_service)
        else:
            print("Booking cancelled.")
            return

        if user is None:
            print("Booking cancelled.")
            return
    start_date = get_valid_date("Enter start date (DD-MM-YYYY): ")
    end_date = get_valid_date("Enter end date (DD-MM-YYYY): ")

    num_days = (end_date - start_date).days
    if num_days <= 0:
        print("End date must be after start date.")
        return

    if num_days < selected_car.min_period or num_days > selected_car.max_period:
        print(f"This car requires a rental period between {selected_car.min_period} "
              f"and {selected_car.max_period} day(s).")
        return

    rental_fee = num_days * selected_car.daily_rate

    print("\n=== Booking Summary ===")
    print(f"  Car          : {selected_car.make} {selected_car.model} ({selected_car.year})")
    print(f"  Start Date   : {start_date.strftime('%d-%m-%Y')}")
    print(f"  End Date     : {end_date.strftime('%d-%m-%Y')}")
    print(f"  Duration     : {num_days} day(s)")
    print(f"  Daily Rate   : ${selected_car.daily_rate:.2f}")
    print(f"  Rental Fee   : ${rental_fee:.2f}")


    confirm = input("\nDo you want to proceed with this booking? (y/n): ").strip().lower()
    if confirm != "y":
        print("Booking cancelled.")
        return
        
    booking_service.book_car(user, selected_car, start_date, end_date, rental_fee)

def login(auth_service):
    print("\n--- Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    user = auth_service.login(username, password)

    if user is None:
        print("Invalid credentials.")
        return None

    print(f"Welcome back, {username} ({user.role})!")
    return user

def signup_customer(user,user_service):
    print("\n--- Sign Up (Customer) ---")
    name = input("Enter your full name: ").strip()
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
    phone = input("Enter your contact number: ").strip()
    try:
        user = user_service.save(user,name,email,password,phone,role.CUSTOMER.value)
        if user is not None:
            display_acc_creation_success(name, email)
            return user

        return None
    except ValueError as e:
        print(f"Signup failed: {e}")
        return None

def apply_search_filters(cars):

    print("\n--- Search Criteria (press Enter to skip any field) ---")

    make = input("Make (e.g. Toyota): ").strip().lower()
    model = input("Model (e.g. Corolla): ").strip().lower()
    year_input = input("Year (e.g. 2022): ").strip()
    min_price_input = input("Min price per day: ").strip()
    max_price_input = input("Max price per day: ").strip()

    filtered = cars

    if make:
        filtered = [c for c in filtered if make in c.make.lower()]

    if model:
        filtered = [c for c in filtered if model in c.model.lower()]

    if year_input:
        try:
            year = int(year_input)
            filtered = [c for c in filtered if c.year == year]
        except ValueError:
            print("Invalid year entered — skipping year filter.")

    if min_price_input:
        try:
            min_price = float(min_price_input)
            filtered = [c for c in filtered if c.daily_rate >= min_price]
        except ValueError:
            print("Invalid minimum price — skipping that filter.")

    if max_price_input:
        try:
            max_price = float(max_price_input)
            filtered = [c for c in filtered if c.daily_rate <= max_price]
        except ValueError:
            print("Invalid maximum price — skipping that filter.")

    return filtered