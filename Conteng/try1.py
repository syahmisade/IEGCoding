def number_to_words(num):
    # Define dictionaries for words representing numbers
    units = ["", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion", "trillion"]

    # Function to convert a number less than 100 into words
    def convert_less_than_100(n):
        if n < 10:
            return units[n]
        elif n < 20:
            return teens[n - 10]
        else:
            # Correct handling of tens and units
            return tens[n // 10] + ("-" + units[n % 10] if n % 10 != 0 else "")

    if num == 0:
        return "zero"

    # Initialize result as an empty list
    words = []
    # Track position in thousands (0: units, 1: thousands, 2: millions, etc.)
    position = 0

    while num > 0:
        # Process numbers in groups of three digits
        chunk = num % 1000
        if chunk != 0:
            chunk_words = convert_less_than_100(chunk)
            if position > 0:
                # Adjusted position indexing
                chunk_words += " " + thousands[position - 1]
            words.insert(0, chunk_words)
        num //= 1000
        position += 1

    return " ".join(words)


# Test the function
number = int(input("Enter a number to translate into words: "))
print(number_to_words(number))
