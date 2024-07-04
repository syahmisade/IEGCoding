'''
Write a Python class Employee with properties id, name, salary, and department and methods like _init_, calculateSalary, assignDepartment and 
_str_.
Sample Employee Data:
"E7876", "ADAMS", 50000, "ACCOUNTING"
"E7499", "JONES", 45000, "RESEARCH"
"E7900", "MARTIN", 50000, "SALES"
"E7698", "SMITH", 55000, "OPERATIONS"
Use 'assignDepartment' method to change the department of an employee.
Use '_str_' method to print the details of an employee.
Use 'calculateSalary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. 
If the number of hours worked is more than 50, the method computes overtime and adds it to the salary.
Overtime is calculated as following formula: 
overtime = hours_worked - 50 Overtime 
amount = (overtime * (salary / 50))
'''
class Employee:
    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
    
    def assignDepartment(self, department):
        self.department = department
    
    def calculateSalary(self,hoursWorked):
        overtime = 0
        if hoursWorked > 50:
            overtime = hoursWorked - 50
        amount = overtime * (self.salary / 50)
        self.salary = self.salary + amount
        return self.salary
    
    def __str__(self):
        statement = f"Worker's Details: \n"
        statement += f"ID: {self.id}\n"
        statement += f"Name: {self.name}\n"
        statement += f"Salary: RM{self.salary:.2f}\n"
        statement += f"Department: {self.department}"
        return statement

worker1 = Employee("E7876", "ADAMS", 50000, "ACCOUNTING")

worker1.assignDepartment("SALES")
worker1.calculateSalary(100)

# Change from "ACCOUNTING" to "SALES"
# Update the salary including the overtime
print(worker1) 
