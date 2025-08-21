def isleapyear(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False



year = int(input("Enter a year: "))

if isleapyear(year):
    print("It is a leap year")
else:
    print("It is not a leap year")

