###################################################
# MSE800 –  Car Rental System
###################################################

Developer: Passang Lhamo
Programme: Master of Software Engineering
Course: MSE800 Professional Software Engineering
Project: Car Rental System
Year:2026

---

# 1. Project Overview

The Car Rental System is an object oriented software system designed to automate a car rental company.
The system eliminates the need for manual paperwork and offers functionality to manage users, cars, rental bookings, payments and return settlements.

The system has two types of users:

Customer: can register, log in and find available cars, book rentals, and manage their rentals.
Administrator : can control car information, customer rentals, funds and return details.

The system is designed based on the principles of object-oriented programming involving models, services, repositories and application functionality.

---

# 2. Main Features

The Car Rental System provides the following functionality:

### User Management

* Customer sign up
* User login
* Password management
* Customer and administrator roles
* User information management

### Car Management

* View available cars
* Add new cars
* Update car information
* Maintain car rental information

### Rental Booking

* Select a car
* Specify rental dates
* Create rental bookings
* Calculate rental charges
* View booking information

### Rental Management

* View booking details
* Approve or reject bookings
* Manage booking status
* Calculate loyal fees
* Calculate settlement fees (late-return)

---

# 3. System Requirements

Before installing the system, ensure that the following are available:

* Python 3.x (currently using 3.14.2)
* SQLite
* Git (optional, if obtaining the project from a Git repository)
* A Python-compatible IDE or code editor such as Visual Studio Code or PyCharm

No separate database server is required if the system uses the included SQLite database.

---

# 4. Installation and Configuration

## Step 1 – Obtain the Source Code

Download or clone the Car Rental System source-code project. 

For example:

```bash
git clone https://github.com/passanglhamo/car_rental_system.git
```

Alternatively, extract the provided project ZIP file.

---

## Step 2 – Open the Project

Open the file that was extracted in the project folder in a Python programming environment.

Example:

```text
car_rental_system/
```

Make sure the project structure is maintained after extraction.

---

## Step 3 – Create a Virtual Environment

Create a Python virtual environment.

Windows:

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

---

## Step 4 – Install Dependencies

For the packages, install using the following command:

```bash
pip install -r requirements.txt
```

---

## Step 5 – Configure the Database

The system uses SQLite for data persistence.

Make sure that the database configuration is properly set in the database configuration/script files.

If there's a database initialisation script, execute it prior to running the application.

Example:

```bash
python script/database.py
```
---

# 5. Running the Application

Navigate to the directory containing the main application file.

Run:

```bash
python main.py
```

The application should display the main menu.

Follow the options shown by the application to access the available functions.

---

# 6. Using the System

## 6.1 Customer Registration

A new customer can create an account by providing the required information, such as:

* Name
* Email
* Password
* Phone number

After successful registration, the system displays an account-creation confirmation.

---

## 6.2 Login

The user enters their registered email and password.

After successful authentication, the system identifies the user's role and provides the appropriate functionality.

---

## 6.3 Viewing Cars

Customers can view the available cars.

Car information may include:

* Car ID
* Make
* Model
* Year
* Mileage
* Availability
* Minimum period
* Maximum period
* Daily rate 

---

## 6.4 Creating a Booking

A customer selects an available car and provides the required rental information, including the rental period.

The system validates the booking information and calculates the applicable rental fee.

---

## 6.5 Managing Cars

Administrators can:

1. Add a new car.
2. View car information.
3. Update car information.

---

## 6.6 Managing Bookings

Administrators can review customer bookings and manage their status, including approving or rejecting booking requests.

---

## 6.7 Return Settlement

When a car is returned, the system can calculate whether the customer has returned the car after the agreed  end date.

If the vehicle is returned late:

```text
Late Days = Return Date - End Date
```

The applicable settlement fee is then calculated using the configured late-fee rate.

If the car is returned early or on-time, customer will be provided with loyal fee which can be used as discount amount in their next booking:



---

# 7. Project Structure

The project follows a layered structure to separate different responsibilities.

The following is the expected structure; the final file list should be updated to match the actual submitted project.

```text
car_rental_system/
│
├── main.py
├── main_menu.py
├── role_menu.py
│
├── models/
│   ├── BaseEntity.py
│   ├── User.py
│   ├── Car.py
│   ├── enums.py
│   └── Booking.py
│
├── repositories/
│   ├── UserRepository.py
│   ├── CarRepository.py
│   └── BookingRepository.py
│
├── services/
│   ├── AuthServices.py
│   ├── UserService.py
│   ├── CarService.py
│   ├── LoyaltyService.py
│   ├── SettlementService.py
│   └── BookingService.py
├── utils/
│   ├── amount_utils.py
│   ├── booking_utils.py
│   ├── date_utils.py
│   ├── display_utils.py
│   └── password_utils.py
│
├── script/
│   └── database.py
│
├── requirements.txt
│
└── README.md
```

---

# 8. File and Folder Descriptions

| File/Folder            | Purpose                                                                       |
| ---------------------- | ----------------------------------------------------------------------------- |
| `main.py`              | This file is the starting point for Car Rental System.                        |
| `models/`              | This folder includes all the entities and enums.                              |
| `User.py`              | This file contains user's information and it's attributes.                    |
| `Car.py`               | This file contains car's information and it's attributes.                     |
| `Booking.py`           | This file contains booking's information and it's attributes                  |
| `repositories/`        | This folder contains all the repositories.                                    |
| `UserRepository.py`    | This file contain user's data persistence and retrieval.                      |
| `CarRepository.py`     | This file contain car's data persistence and retrieval.                       |
| `BookingRepository.py` | This file contain booking's data persistence and retrieval.                   |
| `services/`            | This folder contain business logic for the application.                       |
| `UserService.py`       | This file contain user-related business operations.                           |
| `CarService.py`        | This file contain car-related business operations.                            |
| `BookingService.py`    | This file contain booking-related business operations.                        |
| `LoyaltyService.py`    | This file contain loyalty-fee-related business operations.                    |
| `SettlementService.py` | This file contain settlement-fee-related business operations.                 |
| `script/database.py`   | This file contain data base script.                                           |
| `requirements.txt`     | This file contain list of external package.                                   |
| `README.md`            | Provides installation, configuration, operation, and developer documentation. |



---

# 9. Database

The system uses a database to persist application information.

The database stores information required for system operations, including:

* Users
* Cars
* Bookings
* Rental information

---

# 10. Error Handling and Validation

The system performs validation to reduce invalid operations.

Examples include:

* Validating user input
* Checking login credentials
* Checking car availability
* Validating rental dates
* Validating booking information
* Handling unsuccessful database operations

The appropriate validation helps maintain data consistency and improves the user experience.

---

# 11. Known Issues and Limitations

This is the first edition and has the following restrictions:

1. The system is a primarily academic/software-engineering project and may need further configuration to enable it to be deployed for production use.
2. SQLite is a good option for the current application but may not be a good choice for a production environment with a lot of users.
3. If features are not implemented as part of a package, they are not included, including online payment gateways, real-time vehicle tracking, mobile applications, and cloud deployment.
4. Additional validation and testing might be needed for production use of the application.
5. If there are any other known bugs that were found during testing, they should be noted here before submission.

Known bugs found in final testing:

None documented at present / add any known bugs to this section before submitting.

---

# 12. Security Considerations

The system has protected the information, and the authentication credentials of the user.

The passwords are stored in an encrypted format. Password hashing has been used when storing authentication credentials.

Used parameterised SQL queries to minimise the dangers of SQL injection.

Only authorised administrator users should have access to administrator functionality.

---

# 13. Testing

The system should be tested using normal, boundary, and invalid inputs.

Important test scenarios include:

* Customer siun up
* Customer login
* Invalid login
* Adding a car
* Updating a car
* Viewing available cars
* Creating a booking
* Invalid rental dates
* Approving a booking
* Rejecting a booking
* Returning a vehicle
* Calculating loyal fees
* Calculating settlement fees


---

# 14. Licensing

This academic project is released for educational and assessment purposes.

**License:** Educational / Academic Use Only

No part of the source code should be copied for re-distribution, or used commercially without proper rights and acknowledgment.

Any third-party libraries used by the project remain subject to their respective licenses.
---

# 15. Developer / Credits

Developer: Passang Lhamo

Programme: Master of Software Engineering

Institution: Yoobee College of Innovation

Course: MSE800 Professional Software Engineering

The Car Rental System was developed as an individual academic project to demonstrate object-oriented programming and software engineering principles.

---

# 16. Future Improvements

Potential future enhancements include:

* Online payment integration
* Mobile application
* Cloud deployment
* Email/SMS booking notifications
* Advanced reporting and analytics
* Smart car recommendations
* Demand-based rental pricing
* Real-time vehicle availability
* Automated maintenance reminders
* Improved security and authentication
* Automated testing and CI/CD

---

# 17. Support

For issues with installation or operation, first verify:

1. Python is correctly installed properly.
3. The required dependencies have been installed.
4. The database has been initialised.
5. The project folder structure has not been changed.
6. The application is being started from the correct directory.

For development-related issues, inspect the relevant service, repository, model, or database component based on the error message.

---

# 18. Conclusion

The Car Rental System is an object-oriented approach to the automation of essential processes in a car rental system. It offers functionality such as user management, car management, rental booking, booking management, rental fee calculation, and settlement.

The hierarchical project structure isolates application logic, business services, data access, and domain models, resulting in a better project architecture that helps make the system easier to understand, maintain, test, and extend.

This README is designed to give information to users and programmers on how the Car Rental System can be configured, operated, understood and maintained.
