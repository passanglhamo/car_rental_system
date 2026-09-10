from role_menu import system_admin_menu, admin_menu, customer_menu 
from models.enums import role 
from utils.display_utils import display_car_list
from utils.booking_utils import browse_and_book,login,signup_customer

def route_user(user, car_service,user_service,booking_service,auth_service):
    if user.role == role.SYSTEM_ADMIN.value:
        system_admin_menu(user,user_service)
    elif user.role == role.ADMIN.value:
        admin_menu(user, car_service,booking_service)
    elif user.role == role.CUSTOMER.value:
        customer_menu(user, car_service,auth_service,user_service, booking_service)
    else:
        print(f"Unknown role: {user.role.value}")

def main_menu(user,car_service, auth_service,user_service,booking_service):
    while True:
        display_car_list(car_service.find_by_limit(5), "Latest Cars")

        print("\n--- Main Menu ---")
        print("1. Browse all cars")
        print("2. Login")
        print("3. Sign up (Customer)")
        print("4. Exit")
        entry_choice = input("Select an option: ").strip()

        if entry_choice == "1":
            browse_and_book(user,car_service,auth_service,user_service,booking_service)

        elif entry_choice == "2":
            user = login(auth_service)
            if user:
                route_user(user, car_service,user_service,booking_service,auth_service)

        elif entry_choice == "3":
            user = signup_customer(user,user_service)
            if user:
                route_user(user, car_service,user_service,booking_service,auth_service)

        elif entry_choice == "4":
            print("Goodbye!")
            user = None
            break

        else:
            print("Invalid option. Please try again.")





