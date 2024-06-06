'''
Prompts the user to enter the length and width of a rectangle. 
Calculates the area and perimeter of the rectangle. Prints the area and perimeter.
'''
length = int(input("Pick a length for rectangle: "))
width = int(input("Pick a width for rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")
