'''
Lectured by Mr.Jegan

Data type have 2 types:-
1. Primitive data type
    - Mutable
2. Reference data type
    - Immutable

Function also have inner function:
- Inner function can access outer function variable
- Only can be applied for dynamic coding such as python
- About:
    - Cannot call the inner function outside the normal function
    - Inner function only can be called inside the function object

Lambda function:
- Still a function but only applicable for one line function object

'''
# --- Inner Function ------------------------------------------------
def authenticate_user():
    def check_credentials(username, password):
        stored_username = "user123"
        stored_password = "pass123"
        return username == stored_username and password == stored_password

    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if check_credentials(username, password):
            print("Authentication successful!")
            return True
        else:
            print("Authentication failed. Please try again.")

def calculate_simple_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time (in years): "))
    
    interest = (principal * rate * time) / 100
    return interest

# Example usage
if authenticate_user():
    interest = calculate_simple_interest()
    print(f"The calculated simple interest is: RM{interest:.2f}")


#--- lambda function ------------------------------------------------------------

add = lambda a,b:a+b
# OR
def add(a,b):
    return a+b
