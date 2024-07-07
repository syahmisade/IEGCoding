'''
The greatest common divisor (GCD) of two or more integers, which are not all zero, is 
the largest positive integer that divides each of the integers. After the explanation given by 
tuition teacher, now he wants to conduct the small test to check their understanding of GCD concept.
So, help the students by writing a program to find the GCD of Two Numbers.
Input  Format: 
The input consists of two integers.
Output  Format:
The output consists GCD of Two Numbers.
Note: All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output:
Enter the two positive numbers
12
14
GCD:2
'''
print("Enter the two positive numbers")
num1 = int(input())
num2 = int(input())

if num1 == 0 and num2 == 0:
    print("GCD:0")
elif num1 == 0:
    print("GCD:", num2)
elif num2 == 0:
    print("GCD:", num1)
else:
    while num2 != 0:
        num1, num2 = num2, num1 % num2
print("GCD:", num1)
