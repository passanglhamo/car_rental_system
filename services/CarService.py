from dataclasses import replace
from models.Car import Car
from models.enums import status
import uuid
from datetime import date

class CarService:
    def __init__(self, car_repository):
        self.car_repository = car_repository
        self.cars = []

    """Method to get all cars"""
    def find_all(self):
        return self.car_repository.find_all()

    """Method to get latest cars as per limit"""
    def find_by_limit(self, limit):
        return self.car_repository.find_by_limit(limit)

    def find_by_available(self, start_date, end_date):
        return self.car_repository.find_by_available(start_date, end_date)
    
    """Method to get a car by its ID"""
    def get_car_by_id(self, car_id):
        return self.car_repository.find_by_id(car_id)

    """Method to add a new car"""
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

    """Method to update an existing car"""
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

            

    
            