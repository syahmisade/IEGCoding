from datetime import datetime, timezone, timedelta

now = datetime.now()
# formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
formatted_now = now.strftime("%d-%m-%Y")  # string format time
today = datetime.now(timezone.utc)
tomorow = today + timedelta(days=1)

# print(datetime.now())
# print(datetime.now(timezone.utc))
# print(formatted_now)
# print(today)
# print(tomorow)
# print(today.strftime("%d/%m/%Y %H:%M"))

userDate = input("Enter the date in dd/mm/YYYY format: ")
userDate = datetime.strptime(userDate, "%d/%m/%Y")  # string parse time
print(userDate)
