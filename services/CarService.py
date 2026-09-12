from dataclasses import replace
from models.Car import Car
from models.enums import status
import uuid
from datetime import date
"""
    This service class is responsible for managing car-related business operations.

    CarService acts as an intermediate layer between the application
    and CarRepository. It provides functionality to retrieve, add,
    update, and search for cars based on their availability.
"""
class CarService:
    def __init__(self, car_repository):
        self.car_repository = car_repository
        self.cars = []
    """
        method to retrieve all cars from the database.

        Returns:
            list: A list containing all cars.
    """
    def get_all_cars(self):
        return self.car_repository.find_all()

   
    """
        Method to get the latest cars up to the specified limit.

        Args:
            limit (int): Maximum number of cars to return.
                Defaults to 5.

        Returns:
            list[Car]: A list of the latest car records.
    """
    def get_cars_by_limit(self, limit):
        return self.car_repository.find_by_limit(limit)

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
    def get_available_cars(self, start_date, end_date):
        return self.car_repository.find_by_available(start_date, end_date)
    
    """"
            Method to get a car using its ID.
    
            Args:
                car_id (str): Unique identifier of the car.
    
            Returns:
                Car or None: The matching car if found; otherwise None.
    """
    def get_car_by_id(self, car_id):
        return self.car_repository.find_by_id(car_id)

    """
            Method to save a car record to the database.
    
            Args:
                car (Car): Car object containing the details.
                user_id (str): ID of the user creating the car record.
    
            Returns:
                Car: The saved car object.
    """ 
    def save(self,user):
        car = Car(
            id=str(uuid.uuid4()),
            make=input("Enter car make (Eg. Toyota): "),
            model=input("Enter car model (Eg. Corolla): "),
            year=int(input("Enter car year (Eg. 2022): ")),
            mileage=float(input("Enter car mileage (Eg. 35000): ")),
            daily_rate=float(input("Enter car daily rate (eg. 65): ")),
            min_period=int(input("Enter car minimum rental period: ")),
            max_period=int(input("Enter car maximum rental period: ")),
            status=status.ACTIVE.value,
            created_by = user.id,
            created_date= date.today(),
            updated_by= None,
            updated_date= None
        )
        return self.car_repository.save(car,user.id)

    """
          Method to update an existing car record.
  
          Args:
              car_id (str): ID of the car to update.
              updated_car (Car): Car object containing the updated details.
              user_id (str): ID of the user performing the update.
  
          Returns:
              Car: Updated car object.
    """
    def update_car(self, car_id,user):
        existing_car = self.car_repository.find_by_id(car_id)
        if existing_car is None:
            print("No car found with that ID.")
            return None

        print("Leave a field blank to keep its current value.")

        make = input(f"New make [{existing_car.make}]: ").strip()
        model = input(f"New model [{existing_car.model}]: ").strip()

        year_input = input(f"New year [{existing_car.year}]: ").strip()
        mileage_input = input(f"New mileage [{existing_car.mileage}]: ").strip()
        price_input = input(f"New price per day [{existing_car.daily_rate}]: ").strip()
        min_period_input = input(f"New minimum rental period [{existing_car.min_period}]: ").strip()
        max_period_input = input(f"New maximum rental period [{existing_car.max_period}]: ").strip()

        updated_car = replace(
            existing_car,
            make=make or existing_car.make,
            model=model or existing_car.model,
            year=int(year_input) if year_input else existing_car.year,
            mileage=float(mileage_input) if mileage_input else existing_car.mileage,
            daily_rate=float(price_input) if price_input else existing_car.daily_rate,
            min_period=int(min_period_input) if min_period_input else existing_car.min_period,
            max_period=int(max_period_input) if max_period_input else existing_car.max_period,      
            )

        saved_car = self.car_repository.update(car_id, updated_car,user.id)
        return saved_car

            

    
            