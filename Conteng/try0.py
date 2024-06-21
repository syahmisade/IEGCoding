# Input Format:
# The first line of the input is the first date.
# The second line of the input is the second date. 
# Output Format :
# The output is a count of days separated by space with the difference in time in the format "53 days, 5:43:00"(without quotes).
# Refer to sample input and output for further formatting specifications.

# Sample Input and Output 1:
# Jul 1 2014 2:43PM
# Aug 23 2014 8:26PM
# 53 days, 5:43:00

# Sample Input and Output 2:
# Jan 1 2014 2:43PM
# Jul 21 2014 12:43PM
# 200 days, 22:00:00

import datetime
from datetime import datetime as dt
date_format = "%b %d %Y %I:%M%p"
t1 = dt.strptime(input(), date_format)
t2 = dt.strptime(input(), date_format)
delta = t2 - t1
print(f"{delta.days} days,", end=' ')
print(str(delta).split(', ')[1])
