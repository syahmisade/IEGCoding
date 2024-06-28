'''
Write a simple Python function that takes a number(n) as a parameter. 
Then the function prints out the first n rows of Pascal's triangle. 
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
'''

def generate_pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

def print_symmetric_pascals_triangle(rows):
    triangle = generate_pascals_triangle(rows)
    max_width = len(" ".join(map(str, triangle[-1]))) 
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))


# inputNum = int(input("Enter a number for Pascal's triangle: "))
print_symmetric_pascals_triangle(11)
# print(generate_pascals_triangle(11))

def pascalsTri(r):
    tri = []
    
    for row in range(r):
        line = 11**row
        
        listLine = list(str(line))
        tri.append(listLine)
        
    # print(tri)
    return tri

def pspt(r):
    triangle = pascalsTri(r)
    max_width = len(" ".join(map(str, triangle[-1]))) 
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))
    return " "

# pspt(11)
# print(pascalsTri(11))
# contoh = " ".join(map(str,[123]) )
# print(contoh)

# con = list(map(str,[123]))
# print(con)

# cont = list(str(123))
# print(cont)