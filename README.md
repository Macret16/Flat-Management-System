# Flat Management System

Welcome to the Flat Management System (FMS). This system allows users to manage flat bookings, including buying new flats, updating details, canceling bookings, displaying all details, searching for specific details, and calculating prices. This project uses Python and MySQL for managing and storing data.

## Features

- **Buy New Flat**: Allows users to buy new flats by filling in the required details.
- **Update Details**: Users can update their details.
- **Cancel Flat Booking**: Users can cancel their flat booking.
- **Display All Details**: Displays all the flat booking details.
- **Search Details**: Allows users to search for specific details.
- **Calculate Prices**: Calculates the price of flats based on type and design.

## Installation

To set up this project, you need to have Python and MySQL installed on your machine.

1. **Install Python**: You can download and install Python from [here](https://www.python.org/downloads/).

2. **Install MySQL**: You can download and install MySQL from [here](https://dev.mysql.com/downloads/installer/).

3. **Install MySQL Connector for Python**: You can install it using pip.
    ```sh
    pip install mysql-connector-python
    ```

4. **Set up MySQL Database**:
    - Open your MySQL command-line client or MySQL Workbench.
    - Create a new database named `FMS`.

## Usage

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/flat-management-system.git
    cd flat-management-system
    ```

2. **Run the script**:
    - Open a terminal or command prompt.
    - Navigate to the directory where the script is located.
    - Run the script:
        ```sh
        python flat_management_system.py
        ```

3. **Main Menu**:
    - The main menu will be displayed with the following options:
        ```
        +------------------------+
        |        Main Menu       |
        +------------------------+
        | 1. Buy New Flat        |
        | 2. Update Any Detail   |
        | 3. Cancel Flat Booking |    
        | 4. Display All Details |    
        | 5. Search Any Detail   |
        | 6. Calculate Prices    |
        | 7. Exit The Database   |
        +________________________+
        ```

4. **Buying a New Flat**:
    - Select option 1 from the main menu.
    - Follow the prompts to enter your details and choose the flat type and design.

5. **Updating Details**:
    - Select option 2 from the main menu.
    - Follow the prompts to update the necessary details.

6. **Canceling a Flat Booking**:
    - Select option 3 from the main menu.
    - Follow the prompts to cancel a booking.

7. **Displaying All Details**:
    - Select option 4 from the main menu to display all the booking details.

8. **Searching for Specific Details**:
    - Select option 5 from the main menu.
    - Follow the prompts to search for specific details.

9. **Calculating Prices**:
    - Select option 6 from the main menu to calculate the prices based on flat type and design.

10. **Exiting the Database**:
    - Select option 7 from the main menu to exit the database.

## Database Schema

The project uses two tables: `details` and `prices`.

### Table: `details`
- `RegNo` (int): Registration number
- `Name` (varchar(15)): Name of the buyer
- `Occupation` (varchar(15)): Occupation of the buyer
- `PhoneNo` (varchar(15)): Phone number of the buyer
- `Members` (int): Number of family members
- `FlatNo` (int): Flat number
- `FlatType` (varchar(15)): Type of flat (1BHK or 2BHK)
- `FlatDesign` (varchar(15)): Design of the flat (Basic or Furnitured)
- `Price` (varchar(15)): Price of the flat

### Table: `prices`
- `Basic` (int): Basic price
- `Fur` (int): Furnitured price
- `bhk1` (int): 1BHK price
- `bhk2` (int): 2BHK price
- `area_400` (int): Price for 400 sq ft
- `area_800` (int): Price for 800 sq ft

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


Made By - Karan Jaswani
