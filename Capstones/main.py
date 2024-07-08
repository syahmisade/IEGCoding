'''
Main file:
Function:
1. Display list
2. 
'''
def displaycars():
    details = {}

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
            no_platH, brandH, modelH, tahunH, warnaH = line.strip().split(',')
            
    print(f"{no_platH:10}{brandH:12}{modelH:10}{tahunH:<6}{warnaH:10}")
    print("=" * 50)
    for no_plat, car_details in details.items():
        print(f"{no_plat:10}{car_details['Brand']:12}{car_details['Model']:10}{car_details['Year']:<6}{car_details['Color']:10}")
    
displaycars()