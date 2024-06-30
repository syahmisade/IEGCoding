'''
Imran is working as an accountant in St. Mount College. During the salary payment there was some error with MS Excel software and he was unable to view the  amount to be credited to the faculties' account. So help him by writing a program that would read the file and print it in the console.
-----------------------------------------------------------------
Note :
Read the input from the file and print the output in the console.
-----------------------------------------------------------------
Input file name: SalariesDataSet.csv
-----------------------------------------------------------------
Input File Fomat :
List of Professors along with their details. Find below the sample file format.
-----------------------------------------------------------------
S.No,Rank,Discipline,Years since phd,Years service,Sex,Salary
1,Prof,B,19,18,Male,139750
2,Prof,B,20,16,Male,173200
3,AsstProf,B,4,3,Male,79750
4,Prof,B,45,39,Male,115000
5,AssocProf,B,6,6,Male,97000
-----------------------------------------------------------------
Output Format:
Output is a list of “n” items which is read from the input file.
-----------------------------------------------------------------
Sample Input and Output:
S.No;Rank;Discipline;Years since phd;Years service;Sex;Salary
1;Prof;B;19;18;Male;139750
2;Prof;B;20;16;Male;173200
3;AsstProf;B;4;3;Male;79750
4;Prof;B;45;39;Male;115000
5;AssocProf;B;6;6;Male;97000
'''
import csv

def read_and_print_csv(file_name):
    try:
        with open(file_name, mode='r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  # Read the header row
            print(";".join(headers))  # Print the headers with semicolon
            
            for row in csv_reader:
                print(";".join(row))  # Print each row with semicolon
                
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File name
file_name = 'SalariesDataSet.csv'

# Call the function to read and print the CSV file
read_and_print_csv(file_name)
