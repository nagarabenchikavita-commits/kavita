# Function to check if a year is a leap year
def isleapyear(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

# Input from the user
year = int(input("Enter a year: "))

# Check and display the result
if isleapyear(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
