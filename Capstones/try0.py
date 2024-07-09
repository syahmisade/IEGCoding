def collect_maintenance_data():
    details = {}
    headers = []

    with open('maintenance.txt', 'r') as filehandler:
        lines = filehandler.readlines()

    if not lines:
        print("File is empty.")
        return headers, details
    
    headers = lines[0].strip().split(',')

    for index, line in enumerate(lines[1:], start=1):
        # Split the line into components and ensure it has the correct number of fields
        data = line.strip().split(',')
        if len(data) != len(headers):
            print(f"Skipping line {index}: {line.strip()} (Incorrect number of fields)")
            continue

        no_plat, brand, model, year, color, type_, date, parts, reason, updates = data
        details[no_plat] = {
            "Brand": brand,
            "Model": model,
            "Year": int(year),  # Convert year to integer
            "Color": color,
            "Type": type_,
            "Date": date,
            "Parts": parts,
            "Reason": reason,
            "Updates": updates
        }

    return headers, details

def displayCM():
    headers, details = collect_maintenance_data()

    if not headers or not details:
        print("No data to display.")
        return

    # Calculate the maximum width for each column
    column_widths = {header: len(header) for header in headers}

    for no_plat, car_details in details.items():
        for header, value in car_details.items():
            column_widths[header] = max(column_widths[header], len(str(value)))

    column_widths["No.plat"] = max(column_widths["No.plat"], len("No.plat"))

    # Create a format string based on the maximum widths
    header_format = '  '.join([f"{{:<{column_widths[header]}}}" for header in headers])
    row_format = '  '.join([f"{{:<{column_widths[header]}}}" for header in headers])

    # Print the headers
    print(header_format.format(*headers))
    print("=" * sum(column_widths.values()) + "=" * (len(headers) - 1) * 2)

    # Print the rows
    for no_plat, car_details in details.items():
        print(row_format.format(
            no_plat,
            car_details["Brand"],
            car_details["Model"],
            car_details["Year"],
            car_details["Color"],
            car_details["Type"],
            car_details["Date"],
            car_details["Parts"],
            car_details["Reason"],
            car_details["Updates"]
        ))

# Call the function to display the table
displayCM()
