'''
Main file:
Function: (9)
- collectdata() 
    - ONLY collect data from cars.txt
- keyboardInput()
    - return error if input wrong type of data
- validate_date_format()
    - validate tarikh yang di keyin
- maintenanceMenu()
    - semua pasal maintenance
- displaycars() 
    - display cars data
- collectCM()
    - collect data from maintenance.txt
- displayCM()
    - display car maintenance list
- clear_screen()
    - untuk clear screen
- main()
    - main function
'''
from datetime import datetime
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
            no_plat, brand, model, tahun, warna, jenis, tarikh, parts, sebab, update = line.strip().split(',')
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
            headers = line.strip().split(',')
    
    return headers, details, lines

def menuBeforeMaintenance():
    displayCM()
    print("=" * 80)

    while True:
        no_plat = input("Enter the number plate of the car: ").strip()
        if no_plat == "":
            print("No car plate entered. Please try again.")
            continue
        elif no_plat == "exit":
            print("Exiting...")
            break
            
        print("Menu:")
        print("1. Display Selected Cars")
        print("2. Update Maintenance Status")
        print("3. Exit")
        choice = keyboardInput(int, "Enter your choice (1/2/3): ", "Choice must be an integer")
        if choice == 1:
            display_selected_cars(no_plat)
        elif choice == 2:
            updateCM(no_plat)
        elif choice == 3:
            print ("We will go back to Main Menu.")
            main()
        else:
            print("Invalid choice. Please enter a valid option.")

def display_selected_cars(no_plat):
    headers, details, lines = collectCM()
    if no_plat in details:
        car_details = details[no_plat]
        print(f"License Plate: {no_plat}")
        print(f"Brand: {car_details['Brand']}")
        print(f"Model: {car_details['Model']}")
        print(f"Year: {car_details['Year']}")
        print(f"Color: {car_details['Color']}")
        print(f"Type: {car_details['Type']}")

        menuBeforeMaintenance()
    else:
            print("Invalid number plate. Please enter a valid number plate.")

def updateCM(no_plat):
    headers, details, lines = collectCM()
    
    no_platH, brandH, modelH, tahunH, warnaH, jenisH, tarikhH, partsH, sebabH, updateH = headers
    
    print(f"{no_platH:12}{jenisH:12}{tarikhH:12}{partsH:15}{sebabH:20}{updateH:12}")
    print("=" * 73)
    for index, (no_plat, car_details) in enumerate(details.items()):
        print(f"{no_plat:12}{car_details['Type']:12}{car_details['Date']:12}{car_details['Parts']:15}{car_details['Reason']:20}{car_details['Update']:12}")
    
    # Ask user to enter the number plate of the car to update
    
    if no_plat in details:
        car_details = details[no_plat]
        
        print("Select the update status:")
        print("1. Awaiting")
        print("2. In progress")
        print("3. Completed")
        update_choice = keyboardInput(int, "Enter your choice (1/2/3): ", "Choice must be an integer")
        if update_choice == 1:
            updates_of_maintenance = "Awaiting"
        elif update_choice == 2:
            updates_of_maintenance = "In Progress"
        elif update_choice == 3:
            updates_of_maintenance = "Completed"
        else:
            print("Invalid choice. Please choose 1 or 2 or 3.")
            return
        
        # Update the maintenance status in maintenance.txt
        with open('maintenance.txt', 'r') as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            if line.startswith(no_plat):
                lines[index] = f"{no_plat}|{car_details['Brand']}|{car_details['Model']}|{car_details['Year']}|{car_details['Color']}|{car_details['Type']}|{car_details['Date']}|{car_details['Parts']}|{car_details['Reason']}|{updates_of_maintenance}\n"
                break
        with open('maintenance.txt', 'w') as filehandler:
            for line in lines:
                filehandler.write(line)

        print ("Updates are as shown below:")
        print(f"Car with license plate {no_plat} maintenance status has been updated to {updates_of_maintenance}.")

        menuBeforeMaintenance()
    else:
        print("Invalid number plate. Please enter a valid number plate.")

def displayCM():
    headers, details, lines = collectCM()
    
    no_platH, brandH, modelH, tahunH, warnaH, jenisH, tarikhH, partsH, sebabH, updateH = headers
    
    print(f"{no_platH:12}{jenisH:12}{tarikhH:12}{partsH:15}{sebabH:20}{updateH:12}")
    print("=" * 73)
    for no_plat, car_details in details.items():
        print(f"{no_plat:12}{car_details['Type']:12}{car_details['Date']:12}{car_details['Parts']:15}{car_details['Reason']:20}{car_details['Update']:12}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("=" * 50)
    print("\tWelcome to Car Maintenance System")
    print("=" * 50)
    print("1. Display cars that needed maintenance")
    print("2. Add a car into maintenance list")
    print("3. Update status car maintenance")
    print("4. Display schedule service")
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
            menuBeforeMaintenance()
        elif choice == 4:
            pass
        elif choice == 0:
            print("Thank you for using this system. Have a Good Day!")
            exit()
        else:
            print("Invalid choice. Please choose from the options.")
            continue

if __name__ == "__main__":
    main()
