from datetime import datetime,timedelta,date
import os


# Collecting and updating data Functions -------------------------------------------------------------------------------------------------------------------
def keyboardInput(input_type, prompt, error_message):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(error_message)
        except KeyboardInterrupt:
            print("\nInput interrupted. Exiting...")
            exit()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_date_format(date_string):
    try:
        input_date = datetime.strptime(date_string, '%d-%m-%Y').date()
        if input_date >= datetime.now().date():
            return True
        else:
            return False
    except ValueError:
        print(f"Invalid date format: {date_string}. Please use 'DD-MM-YYYY'.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def collectdata():
    details = {}
    headers = []
    lines = []

    try:
        with open('cars.txt', 'r') as filehandler:
            lines = filehandler.readlines()

        for index, line in enumerate(lines):
            line = line.strip()
            if index == 0:
                headers = line.split('|')
            else:
                try:
                    no_plat, brand, model, tahun, warna = line.split('|')
                    details[no_plat] = {
                        "Brand": brand,
                        "Model": model,
                        "Year": int(tahun),
                        "Color": warna
                    }
                except ValueError as e:
                    print(f"Error processing line {index + 1}: {line}. Error: {e}")
                except Exception as e:
                    print(f"Unexpected error processing line {index + 1}: {line}. Error: {e}")

    except FileNotFoundError:
        print("Error: 'cars.txt' file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return headers, details, lines

def collectCM():
    details = {}
    headers = []
    lines = []

    try:
        if os.path.exists('maintenance.txt'):
            with open('maintenance.txt', 'r') as filehandler:
                lines = filehandler.readlines()
            
            for index, line in enumerate(lines):
                line = line.strip()
                if index == 0:
                    headers = line.split('|')
                else:
                    try:
                        no_plat, brand, model, tahun, warna, jenis, tarikh, parts, sebab, update = line.split('|')
                        details[no_plat] = {
                            "Brand": brand,
                            "Model": model,
                            "Year": int(tahun),
                            "Colour": warna,
                            "Type": jenis,
                            "Date": tarikh,
                            "Parts": parts,
                            "Reason": sebab,
                            "Updates": update
                        }
                    except ValueError as e:
                        print(f"Error processing line {index + 1}: {line}. Error: {e}")
                    except Exception as e:
                        print(f"Unexpected error processing line {index + 1}: {line}. Error: {e}")
        else:
            print("Error: 'maintenance.txt' file not found.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return headers, details, lines

def filtersearch():
    try:
        clear_screen()
        displayCM()
        print("Filter Search for Maintenance Records")
        # Ask user which parts they want to filter
        print("Which part would you like to filter?")
        print("1. Brand")
        print("2. Model")
        print("3. Year")
        print("4. Colour")
        print("5. Type of Maintenance")
        print("6. Updates")
        choice = keyboardInput(int, "Enter your choice (1/2/3/4/5/6): ", "Choice must be an integer")
        
        filter_criteria = {}
        
        if choice == 1:
            filter_criteria["Brand"] = input("Enter the brand: ").strip()
        elif choice == 2:
            filter_criteria["Model"] = input("Enter the model: ").strip()
        elif choice == 3:
            filter_criteria["Year"] = input("Enter the year: ").strip()
        elif choice == 4:
            filter_criteria["Colour"] = input("Enter the colour: ").strip()
        elif choice == 5:
            print("1. Regular Maintenance")
            print("2. Preventive Maintenance")
            print("3. Custom Maintenance")
            type_choice = keyboardInput(int, "Enter your choice (1/2/3): ", "Choice must be an integer")
            if type_choice == 1:
                filter_criteria["Type"] = "regular"
            elif type_choice == 2:
                filter_criteria["Type"] = "preventive"
            elif type_choice == 3:
                filter_criteria["Type"] = "custom"
            else:
                clear_screen()
                print("\nInvalid choice. Returning to filter menu.\n")
                return filtersearch()
        elif choice == 6:
            print("1. Awaiting")
            print("2. In Progress")
            print("3. Completed")
            update_choice = keyboardInput(int, "Enter your choice (1/2/3): ", "Choice must be an integer")
            if update_choice == 1:
                filter_criteria["Updates"] = "Awaiting"
            elif update_choice == 2:
                filter_criteria["Updates"] = "In Progress"
            elif update_choice == 3:
                filter_criteria["Updates"] = "Completed"
            else:
                clear_screen()
                print("\nInvalid choice. Returning to filter menu.\n")
                return filtersearch()
        else:
            clear_screen()
            print("\nInvalid choice. Returning to filter menu.\n")
            return filtersearch()
        
        clear_screen()
        displayCM(filter_criteria)
        menufilter()
    
    except Exception as e:
        clear_screen()
        print(f"An unexpected error occurred: {e}")
        menufilter()

def updateCM(no_plat):
    try:
        headers, details, lines = collectCM()

        # Ask user to enter the number plate of the car to update
        if no_plat in details:
            car_details = details[no_plat]
            
            print(f"Select the update status for Car with license plate {no_plat}:")
            print(f"(Current status: {car_details['Updates']})")
            print("1. Awaiting")
            print("2. In Progress")
            print("3. Completed")
            
            update_choice = keyboardInput(int, "Enter your choice (1/2/3): ", "Choice must be an integer")
            
            if update_choice == 1:
                updates_of_maintenance = "Awaiting"
            elif update_choice == 2:
                updates_of_maintenance = "In Progress"
            elif update_choice == 3:
                updates_of_maintenance = "Completed"
            else:
                clear_screen()
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
                    
            clear_screen()
            print("\nUpdates are as shown below:")
            print(f"Car with license plate {no_plat} maintenance status has been updated to {updates_of_maintenance}.\n")

        else:
            clear_screen()
            print("\nInvalid number plate. Please enter a valid number plate.\n")
    except Exception as e:
        clear_screen()
        print(f"An unexpected error occurred: {e}")

def filterCMByDateRange(start_date, end_date):
    try:
        headers, details, lines = collectCM()

        if not headers or not details:
            print("No car maintenance records found.")
            return

        # Convert start_date and end_date to datetime.date objects if they are datetime.datetime objects
        if isinstance(start_date, datetime):
            start_date = start_date.date()
        if isinstance(end_date, datetime):
            end_date = end_date.date()

        # Define relevant headers and their widths
        relevant_headers = ["No.plat", "Type", "Date", "Updates"]
        min_widths = {
            "No.plat": 9,
            "Type": 15,
            "Date": 12,
            "Updates": 10
        }

        # Filter and sort records within the specified date range
        filtered_details = {
            no_plat: car_details
            for no_plat, car_details in details.items()
            if start_date <= datetime.strptime(car_details["Date"], '%d-%m-%Y').date() <= end_date
        }
        sorted_details = sorted(filtered_details.items(), key=lambda item: datetime.strptime(item[1]["Date"], '%d-%m-%Y'))

        # Calculate the necessary column widths based on content
        column_widths = min_widths.copy()
        for no_plat, car_details in sorted_details:
            for header in relevant_headers:
                if header == "No.plat":
                    column_widths[header] = max(column_widths[header], len(no_plat))
                else:
                    column_widths[header] = max(column_widths[header], len(str(car_details[header])))

        # Define the format strings based on the calculated widths
        header_format = '  '.join([f"{{:<{column_widths[header]}}}" for header in relevant_headers])
        row_format = '  '.join([f"{{:<{column_widths[header]}}}" for header in relevant_headers])

        # Print the headers
        print()
        print("=" * (sum(column_widths.values()) + (len(relevant_headers) - 1) * 2))
        print(header_format.format(*relevant_headers))
        print("=" * (sum(column_widths.values()) + (len(relevant_headers) - 1) * 2))

        # Print the rows
        for no_plat, car_details in sorted_details:
            print(row_format.format(
                no_plat,
                car_details["Type"],
                car_details["Date"],
                car_details["Updates"]
            ))
        print("=" * (sum(column_widths.values()) + (len(relevant_headers) - 1) * 2))
        print()

    except Exception as e:
        print(f"An error occurred: {e}")

# Display Functions -----------------------------------------------------------------------------------------------------------------------------------------
def displayCM(filter_criteria=None):
    try:
        headers, details, lines = collectCM()

        if not headers or not details:
            print("No car maintenance records found.")
            return

        # Apply filter criteria if any
        if filter_criteria:
            filtered_details = {k: v for k, v in details.items() if all(str(v.get(key, '')).lower() == str(value).lower() for key, value in filter_criteria.items())}
        else:
            filtered_details = details

        if not filtered_details:
            print("No car maintenance records match the filter criteria.")
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
        for no_plat, car_details in filtered_details.items():
            for header, value in car_details.items():
                column_widths[header] = max(column_widths[header], len(str(value)))
            column_widths["No.plat"] = max(column_widths["No.plat"], len(no_plat))

        # Define the format strings based on the calculated widths
        header_format = '  '.join([f"{{:<{column_widths[header]}}}" for header in headers])
        row_format = '  '.join([f"{{:<{column_widths[header]}}}" for header in headers])

        # Print the headers
        print("=" * (sum(column_widths.values()) + (len(headers) - 1) * 2))
        print(header_format.format(*headers))
        print("=" * (sum(column_widths.values()) + (len(headers) - 1) * 2))

        # Print the rows in the order they appear in the file
        for line in lines[1:]:
            try:
                no_plat, brand, model, tahun, warna, jenis, tarikh, parts, sebab, update = line.strip().split('|')
                if no_plat in filtered_details:
                    car_details = filtered_details[no_plat]
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
            except ValueError as e:
                print(f"Error processing line: {line}. Error: {e}")
                continue

        # Print bottom border
        print("=" * (sum(column_widths.values()) + (len(headers) - 1) * 2))
    
    except FileNotFoundError:
        print("Error: File 'maintenance.txt' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def displayFilteredCM(filter_criteria=None):
    headers, details, lines = collectCM()

    if not headers or not details:
        print("No car maintenance records found.")
        return

    # Define relevant headers and their minimum widths
    relevant_headers = ["No.plat", "Type", "Date", "Updates"]
    min_widths = {
        "No.plat": 9,
        "Type": 15,
        "Date": 12,
        "Updates": 10
    }

    # Calculate column widths based on content
    column_widths = min_widths.copy()
    for no_plat, car_details in details.items():
        for header in relevant_headers:
            if header == "No.plat":
                column_widths[header] = max(column_widths[header], len(no_plat))
            else:
                column_widths[header] = max(column_widths[header], len(str(car_details.get(header, "")) or ""))

    # Define format strings based on calculated widths
    header_format = '  '.join([f"{{:<{column_widths[header]}}}" for header in relevant_headers])
    row_format = '  '.join([f"{{:<{column_widths[header]}}}" for header in relevant_headers])

    # Print headers
    print("=" * (sum(column_widths.values()) + (len(relevant_headers) - 1) * 2))
    print(header_format.format(*relevant_headers))
    print("=" * (sum(column_widths.values()) + (len(relevant_headers) - 1) * 2))

    # Print rows with optional filtering
    if filter_criteria:
        filtered_details = {}
        for no_plat, car_details in details.items():
            match = True
            for key, value in filter_criteria.items():
                if str(car_details.get(key, "")).lower() != str(value).lower() and no_plat != value:
                    match = False
                    break
            if match:
                filtered_details[no_plat] = car_details
    else:
        filtered_details = details

    if not filtered_details:
        print("No car maintenance records match the filter criteria.")
    else:
        for no_plat, car_details in filtered_details.items():
            print(row_format.format(
                no_plat,
                car_details["Type"],
                car_details["Date"],
                car_details["Updates"]
            ))
    print("=" * (sum(column_widths.values()) + (len(relevant_headers) - 1) * 2))

def display_selected_cars(no_plat):
    headers, details, lines = collectCM()
    if no_plat in details:
        car_details = details[no_plat]
        print()
        print("=" * 50)
        print(f"Car Details for License Plate: {no_plat}")
        print("-" * 50)
        print(f"Brand: {car_details['Brand'].ljust(20)}")
        print(f"Model: {car_details['Model'].ljust(20)}")
        print(f"Year: {str(car_details['Year']).ljust(20)}")
        print(f"Colour: {car_details['Colour'].ljust(20)}")
        print(f"Type: {car_details['Type'].ljust(20)}")
        print(f"Date: {car_details['Date'].ljust(20)}")
        print(f"Parts to fix: {car_details['Parts'].ljust(20)}")
        print(f"Reason of maintenance: {car_details['Reason'].ljust(20)}")
        print(f"Updates: {car_details['Updates'].ljust(20)}")
        print("=" * 50)
        print()
    else:
        print("\nInvalid number plate. Please enter a valid number plate.\n")

def displayThisWeekCM():
    try:
        today = datetime.now()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        filterCMByDateRange(start_of_week, end_of_week)
    except Exception as e:
        print(f"An error occurred: {e}")

def displaythisMonthCM():
    try:
        today = datetime.now()
        start_of_month = today.replace(day=1)
        if today.month == 12:
            end_of_month = today.replace(year=today.year + 1, month=1, day=1) - timedelta(days=1)
        else:
            end_of_month = today.replace(month=today.month + 1, day=1) - timedelta(days=1)
        filterCMByDateRange(start_of_month, end_of_month)
    except Exception as e:
        print(f"An error occurred: {e}")

def displayNextMonthCM():
    try:
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
    except Exception as e:
        print(f"An error occurred: {e}")

# Menus Functions --------------------------------------------------------------------------------------------------------------------------------------------
def menuCMS():
    print("This week schedule: ")
    displayThisWeekCM()
    while True:
        try:
            print("Schedule Menu:")
            print("1. Car Details")
            print("2. This Week")
            print("3. This Month")
            print("4. Next Month")
            print("5. Main Menu")
            print("0. Exit")
            
            choice = keyboardInput(int, "Enter your choice (1/2/3/4/5/0): ", "Choice must be an integer")
            
            if choice == 1:
                no_plat = input("Enter the number plate of the car: ").strip()
                if not no_plat:
                    clear_screen()
                    print("\nNo car plate entered. Please try again.\n")
                    continue
                clear_screen()
                display_selected_cars(no_plat)
                
            elif choice == 2:
                clear_screen()
                print("This week schedule: ")
                displayThisWeekCM()
                
            elif choice == 3:
                clear_screen()
                print("This month schedule: ")
                displaythisMonthCM()
                
            elif choice == 4:
                clear_screen()
                print("Next month schedule: ")
                displayNextMonthCM()
                
            elif choice == 5:
                main()
                break
                
            elif choice == 0:
                clear_screen()
                exit()
                
            else:
                clear_screen()
                print("Invalid choice. Please enter a valid option.")
        
        except ValueError:
            clear_screen()
            print("Invalid input. Please enter a valid integer choice.")
        
        except Exception as e:
            clear_screen()
            print(f"An error occurred: {e}")

def menuBeforeMaintenance():
    while True:
        try:
            displayFilteredCM()
            print("Menu:")
            print("1. Display Selected Cars")
            print("2. Update Maintenance Status")
            print("3. Main Menu")
            print("0. Exit")
            
            choice = keyboardInput(int, "Enter your choice (1/2/3/0): ", "Choice must be an integer")

            if choice == 1:
                no_plat_1 = input("Enter the number plate of the car for display: ").strip()
                if not no_plat_1:
                    clear_screen()
                    print("\nNo car plate entered. Please try again.\n")
                    continue
                elif no_plat_1.lower() == "exit":
                    print("Exiting...")
                    break
                clear_screen()
                display_selected_cars(no_plat_1)
                
            elif choice == 2:
                no_plat_2 = input("Enter the number plate of the car for update: ").strip()
                if not no_plat_2:
                    clear_screen()
                    print("\nNo car plate entered. Please try again.\n")
                    continue
                elif no_plat_2.lower() == "exit":
                    print("Exiting...")
                    break
                clear_screen()
                updateCM(no_plat_2)
                
            elif choice == 3:
                print("Returning to Main Menu...")
                main()
                break
                
            elif choice == 0:
                clear_screen()
                exit()
                
            else:
                clear_screen()
                print("Invalid choice. Please enter a valid option.")
        
        except ValueError:
            clear_screen()
            print("Invalid input. Please enter a valid integer choice.")
        
        except Exception as e:
            clear_screen()
            print(f"An error occurred: {e}")

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
    clear_screen()
    
    # Check if the chosen license plate exists in the details
    if no_plat in details:
        car_details = details[no_plat]
        
        choice = -1
        while choice != 0:
            print("=" * 60)
            print(f"Maintenance for car with license plate number {no_plat}")
            print("=" * 60)

            options = [
                "1. Regular Maintenance",
                "2. Preventive Maintenance",
                "3. Custom Schedules",
                "0. Exit"
            ]

            for option in options:
                print(f"{option}")
            print("=" * 60)

            choice = keyboardInput(int, "Choice (1, 2, 3, 0): ", "Choice must be an integer")
            if choice == 1:
                type_of_maintenance = "regular"
            elif choice == 2:
                type_of_maintenance = "preventive"
            elif choice == 3:
                type_of_maintenance = "custom"
            elif choice == 0:
                main()
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
            
            # Remove the car from the lines list
            updated_lines = [line for line in lines if not line.startswith(no_plat)]
            
            # Write the updated list back to cars.txt
            with open('cars.txt', 'w') as filehandler:
                for line in updated_lines:
                    filehandler.write(line)
            
            clear_screen()
            print(f"\nCar with license plate {no_plat} has been added to maintenance list.\n")
            break
    else:
        print(f"No car with license plate {no_plat} found.")

def menufilter():
    while True:
        print("Menu:")
        print("1. Filter List")
        print("2. Maintenance List")
        print("3. Main Menu")
        print("0. Exit")
        
        choice = keyboardInput(int, "Enter your choice (1/2/3/0): ", "Choice must be an integer")
        
        if choice not in [1, 2, 3, 0]:
            clear_screen()
            print("\nInvalid choice. Please enter a valid option.\n")
            continue
        
        if choice == 2:
            clear_screen()
            displayCM()
        elif choice == 1:
            clear_screen()
            filtersearch()
            # Ensure that after filtering, the user returns to the menu
            input("\nPress Enter to return to the Menu...")
            clear_screen()
        elif choice == 3:
            print("Returning to Main Menu.")
            main()
            break
        elif choice == 0:
            clear_screen()
            exit()

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
            menufilter()
        elif choice == 2:
            clear_screen()
            maintenanceMenu()
        elif choice == 3:
            clear_screen()
            menuBeforeMaintenance()
        elif choice == 4:
            clear_screen()
            menuCMS()
        elif choice == 0:
            clear_screen()  
            exit()
        else:
            print("Invalid choice. Please choose from the options.")
            continue

# Running Main -------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
