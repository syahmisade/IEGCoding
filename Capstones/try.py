from datetime import datetime
import os

def collectdata():
    details = {}
    headers = []

    with open('cars.txt', 'r') as filehandler:
        lines = filehandler.readlines()
    for index, line in enumerate(lines):
        if index > 0:
            no_plat, brand, model, tahun, warna = line.strip().split('|')
            details[no_plat] = {
                "Brand": brand,
                "Model": model,
                "Year": int(tahun),  # Convert year to integer
                "Color": warna
            }
        elif index == 0:
            headers = line.strip().split('|')
    
    return headers, details, lines

def keyboardInput(input_type, prompt, error_message):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(error_message)

def validate_date_format(date_string):
    try:
        # datetime.strptime(date_string, '%d-%m-%Y')
        if datetime.strptime(date_string, '%d-%m-%Y').date() >= datetime.now().date():
            return True
        else:
            return False
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
            with open('maintenance.txt', 'a+') as maintenance_file:
                maintenance_file.seek(0)  # Move to the beginning of the file
                first_char = maintenance_file.read(1)
                if not first_char:
                    # File is empty, write headers
                    maintenance_file.write(f"{no_platH}|{brandH}|{modelH}|{tahunH}|{warnaH}|Type|Date|Parts|Reason|Updates\n")
                else:
                    # File already has content, move back to end of file
                    maintenance_file.seek(0, os.SEEK_END)
                
                maintenance_file.write(
                    f"{no_plat}|{car_details['Brand']}|{car_details['Model']}|{car_details['Year']}|{car_details['Color']}|"
                    f"{type_of_maintenance}|{date_of_maintenance}|{parts_to_fix}|{reason_for_maintenance}|{updates_of_maintenance}\n"
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
    
    if os.path.exists('maintenance.txt'):
        with open('maintenance.txt', 'r') as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            if index > 0:
                no_plat, brand, model, tahun, warna, jenis, tarikh, parts, sebab, update = line.strip().split('|')
                details[no_plat] = {
                    "Brand": brand,
                    "Model": model,
                    "Year": int(tahun),  # Convert year to integer
                    "Colour": warna,
                    "Type": jenis,
                    "Date": tarikh,
                    "Parts": parts,
                    "Reason": sebab,
                    "Updates": update
                }
            elif index == 0:
                headers = line.strip().split('|')
    
    return headers, details, lines if 'lines' in locals() else []

def displayCM():
    headers, details, lines = collectCM()

    if not headers or not details:
        print("No car maintenance records found.")
        return
    
    # Set minimum column widths
    min_widths = {
        "No.plat": 9,
        "Brand": 9,
        "Model": 9,
        "Year": 6,
        "Colour": 12,
        "Type": 15,
        "Date": 12,
        "Parts": 15,
        "Reason": 20,
        "Updates": 10
    }

    # Calculate the necessary column widths based on content
    column_widths = min_widths.copy()
    for no_plat, car_details in details.items():
        for header, value in car_details.items():
            column_widths[header] = max(column_widths[header], len(str(value)))
        column_widths["No.plat"] = max(column_widths["No.plat"], len(no_plat))

    # Define the format strings based on the calculated widths
    header_format = '  '.join([f"{{:<{column_widths[header]}}}" for header in headers])
    row_format = '  '.join([f"{{:<{column_widths[header]}}}" for header in headers])

    # Print the headers
    print(header_format.format(*headers))
    print("=" * (sum(column_widths.values()) + (len(headers) - 1) * 2))

    # Print the rows
    for no_plat, car_details in details.items():
        print(row_format.format(
            no_plat,
            car_details["Brand"],
            car_details["Model"],
            car_details["Year"],
            car_details["Colour"],
            car_details["Type"],
            car_details["Date"],
            car_details["Parts"],
            car_details["Reason"],
            car_details["Updates"]
        ))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
        print("3. Main Menu")
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
        print(f"Colour: {car_details['Colour']}")
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
        print(f"{no_plat:12}{car_details['Type']:12}{car_details['Date']:12}{car_details['Parts']:15}{car_details['Reason']:20}{car_details['Updates']:12}")
    
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
                lines[index] = f"{no_plat}|{car_details['Brand']}|{car_details['Model']}|{car_details['Year']}|{car_details['Colour']}|{car_details['Type']}|{car_details['Date']}|{car_details['Parts']}|{car_details['Reason']}|{updates_of_maintenance}\n"
                break
        with open('maintenance.txt', 'w') as filehandler:
            for line in lines:
                filehandler.write(line)

        print ("Updates are as shown below:")
        print(f"Car with license plate {no_plat} maintenance status has been updated to {updates_of_maintenance}.")

        menuBeforeMaintenance()
    else:
        print("Invalid number plate. Please enter a valid number plate.")

def displayCMS():
    headers, details, lines = collectCM()
    
    no_platH, brandH, modelH, tahunH, warnaH, jenisH, tarikhH, partsH, sebabH, updateH = headers
    
    # Convert date strings to datetime objects and sort the details by date in descending order
    sorted_details = sorted(details.items(), key=lambda item: datetime.strptime(item[1]["Date"], '%d-%m-%Y'), reverse=True)

    print(f"{no_platH:12}{jenisH:12}{tarikhH:12}{partsH:15}{sebabH:20}{updateH:12}")
    print("=" * 73)
    for no_plat, car_details in sorted_details:
        print(f"{no_plat:12}{car_details['Type']:12}{car_details['Date']:12}{car_details['Parts']:15}{car_details['Reason']:20}{car_details['Updates']:12}")

def main():
    clear_screen()
    print("=" * 50)
    print("\tWelcome to Car Maintenance System")
    choice = -1
    while choice != 0:
        print("=" * 50)
        print("1. Display cars that needed maintenance")
        print("2. Add a car into maintenance list")
        print("3. Update status car maintenance")
        print("4. Display schedule service")
        print("0. Exit")
        print("=" * 50)
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
            clear_screen()
            displayCMS()
        elif choice == 0:
            clear_screen()  
            exit()
        else:
            print("Invalid choice. Please choose from the options.")
            continue

if __name__ == "__main__":
    main()