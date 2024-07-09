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
                "Colour": warna,
                "Type": jenis,
                "Date": tarikh,
                "Parts": parts,
                "Reason": sebab,
                "Updates": update
            }
        elif index == 0:
            headers = line.strip().split(',')
    
    return headers, details, lines

def displayCM():
    headers, details, _ = collectCM()

    if not headers or not details:
        print("No car maintenance records found.")
        return

    # no_platH, brandH, modelH, tahunH, warnaH, jenisH, tarikhH, partsH, sebabH, updateH = headers

    # Set minimum column widths
    min_widths = {
        "No.plat": 12,
        "Brand": 12,
        "Model": 12,
        "Year": 6,
        "Colour": 12,
        "Type": 15,
        "Date": 12,
        "Parts": 15,
        "Reason": 20,
        "Updates": 20
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

displayCM()