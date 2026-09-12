import sqlite3

from psutil import users
from script.database import create_tables,insert_data,delete_admin

from repositories.CarRepository import CarRepository
from repositories.UserRepository import UserRepository
from repositories.BookingRepository import BookingRepository

from services.AuthService import AuthService
from services.UserService import UserService
from services.CarService import CarService
from services.BookingService import BookingService
from services.LoyaltyService import LoyaltyService

from main_menu import main_menu

DB_PATH = "car_rental_system.db"

def main():
    print("Welcome to the Car Rental System!")
    db = sqlite3.connect(DB_PATH)
    car_repository = CarRepository(db)
    user_repository = UserRepository(db)
    booking_repository = BookingRepository(db)

    user=None

    car_service = CarService(car_repository)
    user_service = UserService(user_repository)
    auth_service = AuthService(user_service)
    loyalty_service=LoyaltyService()
    booking_service = BookingService(car_repository,booking_repository,user_repository)  
    main_menu(user,car_service, auth_service,user_service,booking_service,loyalty_service)  
       

if __name__ == "__main__":
    create_tables()
    insert_data()
    main()
