'''
RegExr.com


'''
# .ASCII or re.A: When this flag is used, the regular expression operates in ASCII mode, meaning that:
# \w matches [a-zA-Z0-9_] (ASCII word characters).
# \W matches [^a-zA-Z0-9_] (non-ASCII word characters).
# \d matches [0-9] (ASCII digits).
# \D matches [^0-9] (non-ASCII digits).
# \s matches [ \t\n\r\f\v] (ASCII whitespace characters).
# \S matches [^\s] (non-ASCII whitespace characters)
import re

email = "syhmiisade@gmail.com"
expression = r"[a-z\.]+"  # raw string

matches = re.findall(expression, email)
name = matches[0]
domain = matches[1]

# print(matches)
# print(name)
# print(domain)

# -------------------------------------------------

print(f"\nOther example")
price = "Price: $1,453.50"
expression = r"Price: \$([0-9,]*\.[0-9]{2})"

matches = re.search(expression, price)

if matches:
    print(matches.group(0))  # Entire match
    print(matches.group(1))  # First thing in brackets

    withoutcomma = matches.group(1).replace(",", "")
    priceNum = float(withoutcomma)
    print(priceNum)
else:
    print("No match found")
