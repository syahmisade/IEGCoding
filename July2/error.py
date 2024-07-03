try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print("Result is", result)
    # except ValueError:
    #     print("Invalid input! Please enter a valid number.")
    # except ZeroDivisionError:
    #     print("Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error occurred: {e}")
else:
    print("No exceptions occurred.")
finally:
    print("This block is executed no matter what.")
