def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


year = int(input("Enter a year: "))

print("It is a leap year" if is_leap_year(year) else "It is not a leap year")
