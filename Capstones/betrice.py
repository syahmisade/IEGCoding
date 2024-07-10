from datetime import datetime, timedelta
import os

def collectdata():
    details = {}
    headers = []

    with open('cars.txt', 'r') as filehandler:
        lines = filehandler.readlines()
    for index, line in enumerate(lines):
        if index > 0:
            no_plat, brand, model, tahun, warna = line.strip().split(',')
            details[no_plat] = {
                "Brand": brand,
                "Model": model,
                "Year": int(tahun),  # Convert year to integer
                "Color": warna
            }
        elif index == 0:
            headers = line.strip().split(',')
    
    return headers, details, lines

def keyboardInput(input_type, prompt, error_message):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(error_message)

def validate_date_format(date_string):
    try:
        datetime.strptime(date_string, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def maintenanceMenu():
    headers, details, lines = collectdata()
    
    # Extract headers
    no_platH, brandH, modelH, tahunH, warnaH = headers
    
    # Display car list
    print(f"{no_platH:10}{brandH:12}{modelH:10}{tahunH:<6}{warnaH:10}")
    print("=" * 50)
    for no_plat, car_details in details.items():
        print(f"{no_plat:10}{car_details['Brand']:12}{car_details['Model']:10}{car_details['Year']:<6}{car_details['Color']:10}")
    
    # Ask user to pick a car by license plate number
    no_plat = input(f"\nEnter the license plate number of the car to put in maintenance: ").strip()
    
    # Check if the chosen license plate exists in the details
    if no_plat in details:
        car_details = details[no_plat]
        
        choice = -1
        while choice != 0:
            print("=" * 60)
            print("\t\t\tMaintenance")
            print("=" * 60)

            options = [
                "1. Regular Maintenance",
                "2. Preventive Maintenance",
                "3. Custom Schedules",
                "0. Exit"
            ]

            for option in options:
                print(f"\t\t{option}")
            print("=" * 60)

            choice = keyboardInput(int, "Choice (1, 2, 3, 0): ", "Choice must be an integer")
            if choice == 1:
                type_of_maintenance = "regular"
            elif choice == 2:
                type_of_maintenance = "preventive"
            elif choice == 3:
                type_of_maintenance = "custom"
            elif choice == 0:
                return None
            else:
                print("Invalid choice. Please choose from the options.")
                continue
            
            # Collect date of maintenance with validation
            while True:
                date_of_maintenance = input("Enter the date of maintenance (DD-MM-YYYY): ").strip()
                if validate_date_format(date_of_maintenance):
                    break
                else:
                    print("Invalid date format. Please enter the date in DD-MM-YYYY format.")
            
            parts_to_fix = input("Enter the parts to fix: ").strip()
            reason_for_maintenance = input("Enter the reason for maintenance: ").strip()
            updates_of_maintenance = "Awaiting"  # Default value
            
            # Append the selected car's details to maintenance.txt
            with open('maintenance.txt', 'a') as maintenance_file:
                # Check if the file is empty to write headers
                if maintenance_file.tell() == 0:
                    maintenance_file.write(f"{no_platH},{brandH},{modelH},{tahunH},{warnaH},Type,Date,Parts,Reason,Updates\n")
                
                maintenance_file.write(
                    f"{no_plat},{car_details['Brand']},{car_details['Model']},{car_details['Year']},{car_details['Color']},"
                    f"{type_of_maintenance},{date_of_maintenance},{parts_to_fix},{reason_for_maintenance},{updates_of_maintenance}\n"
                )
            
            print(f"Car with license plate {no_plat} has been added to maintenance.txt.")
            
            # Remove the car from the lines list
            updated_lines = [line for line in lines if not line.startswith(no_plat)]
            
            # Write the updated list back to cars.txt
            with open('cars.txt', 'w') as filehandler:
                for line in updated_lines:
                    filehandler.write(line)
            
            print(f"Car with license plate {no_plat} has been removed from cars.txt.")
            break
    else:
        print(f"No car with license plate {no_plat} found.")

def displaycars():
    headers, details, lines = collectdata()

    no_platH, brandH, modelH, tahunH, warnaH = headers
    
    print(f"{no_platH:10}{brandH:12}{modelH:10}{tahunH:<6}{warnaH:10}")
    print("=" * 50)
    
    for no_plat, car_details in details.items():
        print(f"{no_plat:10}{car_details['Brand']:12}{car_details['Model']:10}{car_details['Year']:<6}{car_details['Color']:10}")

def collectCM():
    details = {}
    headers = []
    
    with open('maintenance.txt', 'r') as filehandler:
        lines = filehandler.readlines()
    for index, line in enumerate(lines):
        if index > 0:
            no_plat, brand, model, tahun, warna, jenis, tarikh, parts, sebab, update = line.strip().split('|')
            details[no_plat] = {
                "Brand": brand,
                "Model": model,
                "Year": int(tahun),  # Convert year to integer
                "Color": warna,
                "Type": jenis,
                "Date": tarikh,
                "Parts": parts,
                "Reason": sebab,
                "Update": update
            }
        elif index == 0:
            headers = line.strip().split('|')
    
    return headers, details, lines

def displayCM():
    headers, details, lines = collectCM()
    
    no_platH, brandH, modelH, tahunH, warnaH, jenisH, tarikhH, partsH, sebabH, updateH = headers
    
    # Convert date strings to datetime objects and sort the details by date in descending order
    sorted_details = sorted(details.items(), key=lambda item: datetime.strptime(item[1]["Date"], '%d-%m-%Y'), reverse=True)

    print(f"{no_platH:12}{jenisH:12}{tarikhH:12}{partsH:15}{sebabH:20}{updateH:12}")
    print("=" * 73)
    for no_plat, car_details in sorted_details:
        print(f"{no_plat:12}{car_details['Type']:12}{car_details['Date']:12}{car_details['Parts']:15}{car_details['Reason']:20}{car_details['Update']:12}")

def filterCMByDateRange(start_date, end_date):
    headers, details, lines = collectCM()
    
    no_platH, brandH, modelH, tahunH, warnaH, jenisH, tarikhH, partsH, sebabH, updateH = headers
    
    # Filter records within the specified date range
    filtered_details = {
        no_plat: car_details
        for no_plat, car_details in details.items()
        if start_date <= datetime.strptime(car_details["Date"], '%d-%m-%Y') <= end_date
    }
    
    sorted_details = sorted(filtered_details.items(), key=lambda item: datetime.strptime(item[1]["Date"], '%d-%m-%Y'))

    print(f"{no_platH:12}{jenisH:12}{tarikhH:12}{partsH:15}{sebabH:20}{updateH:12}")
    print("=" * 73)
    for no_plat, car_details in sorted_details:
        print(f"{no_plat:12}{car_details['Type']:12}{car_details['Date']:12}{car_details['Parts']:15}{car_details['Reason']:20}{car_details['Update']:12}")

def displayThisWeekCM():
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    filterCMByDateRange(start_of_week, end_of_week)

def displaythisMonthCM():
    today = datetime.now()
    start_of_month = today.replace(day=1)
    if today.month == 12:
        end_of_month = today.replace(year=today.year + 1, month=1, day=1) - timedelta(days=1)
    else:
        end_of_month = today.replace(month=today.month + 1, day=1) - timedelta(days=1)
    filterCMByDateRange(start_of_month, end_of_month)

def displayNextMonthCM():
    today = datetime.now()
    if today.month == 12:
        start_of_next_month = today.replace(year=today.year + 1, month=1, day=1)
        end_of_next_month = start_of_next_month.replace(year=today.year + 1, month=2, day=1) - timedelta(days=1)
    else:
        start_of_next_month = today.replace(month=today.month + 1, day=1)
        if today.month == 11:
            end_of_next_month = today.replace(year=today.year, month=12, day=31)
        else:
            end_of_next_month = today.replace(month=today.month + 2, day=1) - timedelta(days=1)
    filterCMByDateRange(start_of_next_month, end_of_next_month)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("=" * 50)
    print("\tWelcome to Car Maintenance System")
    print("=" * 50)
    print("1. Display all maintenance records")
    print("2. Add a car to maintenance list")
    print("3. Display weekly maintenance schedule")
    print("4. Display monthly maintenance schedule")
    print("0. Exit")
    print("=" * 50)
    choice = -1
    while choice != 0:
        choice = keyboardInput(int, "Choice (1, 2, 3, 4, 0): ", "Choice must be an integer")
        if choice == 1:
            clear_screen()
            displayCM()
        elif choice == 2:
            clear_screen()
            maintenanceMenu()
        elif choice == 3:
            clear_screen()
            displayThisWeekCM()
        elif choice == 4:
            clear_screen()
            displaythisMonthCM()
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please choose from the options.")
            continue

# if __name__ == "__main__":
#     main()
displayThisWeekCM()
print()
displaythisMonthCM()
print()
displayNextMonthCM()
