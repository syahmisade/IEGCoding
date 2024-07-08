'''
Madhumitha was working as an Accountant in BINNI mills Pvt Ltd, Coimbatore. She was in charge of 
crediting salary for all the employees, summarising the current financial status by collecting 
information, preparing balance sheet, profit, and loss statement, and other reports.
That particular day she was assigned to generate a report that contains the Date of Joining of 
employees between years 1980 - 2015 in the format (yyyy, MMM,dd). But the date of joining which 
is available in the present datasheet is in the format DD-MMM-YY. Help her to convert the 
date of joining of all the employees to (DD, MMM, yyyy) format by writing a program.
Note :
Create a dictionary suitable for decoding month names to numbers.
Months in a dictionary should be in the following format: JAN for January, FEB for February, 
MAR for March and so on..
Create a  function named date_decoder( ) that takes a date in the "dd-MMM-yy" format as 
its argument. Translate the month, correct the year to include all of the digits and 
respond with the format of (yyyy,MMM,dd).
Input format:
Input is a string that contains the date in the format DD-MMM-YY format.
Output format :
The output is the translated form of the input date string in 
the format (yyyy, MMM, dd) as a tuple.
and display whether the year is a leap year or not
Note: Refer to sample input and output for further formatting specifications.
Sample Input 1 :
85-MAR-19
Sample Output 1 :
(19, 03, 1985) is not a leap year
Sample Input 2 :
04-DEC-12
Sample Output 2 :
(12, 12, 2004) is a leap year
'''
from datetime import datetime, timezone, timedelta

# userDate = input("Enter the date in dd-mm-YYYY format: ")
# # Parse string to datetime object
# userDate = datetime.strptime(userDate, "(%d, %m, %Y)")
# userDate_only_date = userDate.date()  # Extract date part
# print(userDate_only_date)

# user_date = input("Enter the date in dd-MMM-YY format (e.g., 04-DEC-12): ")

# input_format = "%y-%b-%d"
# output_format = "(%d, %m, %Y)"

# parsed_date = datetime.strptime(user_date, input_format)

# formatted_date = parsed_date.strftime(output_format)

# print(formatted_date)
# -----------------------------------------------------------------------------


def dateVar(date):
    monthDict = {
        "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6,
        "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12
    }

    year, month, day = date.split("-")
    year = int(year)
    month = monthDict[month]
    day = int(day)

    return (year, month, day)


def leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# def main():
#     date = input()
#     year, month, day = dateVar(date)
#     if leapYear(year):
#         print(f"({day}, {month}, {year}) is a leap year")
#     else:
#         print(f"({day}, {month}, {year}) is not a leap year")


# if __name__ == "__main__":
#     main()

# -----------------------------------------------------------------
def date_decoder():
    date_str = input()
    year, month_abbr, day = date_str.split("-")
    year = int(year)
    if year <= 21:
        year += 2000
    else:
        year += 1900

    month_dict = {
        "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6,
        "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12
    }
    month = month_dict[month_abbr]

    return year, month, int(day)


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def main():
    year, month, day = date_decoder()
    is_leap = leap_year(year)

    print(f"({day:02}, {month:02}, {year}) is {
          'a leap year' if is_leap else 'not a leap year'}")


if __name__ == "__main__":
    main()
