def leapyearsinrange(sr year, er year):
    leapyears = []
    for year in range(sr year, er year + 1):
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            leapyears.append(year)
    return leapyears


start = int(input("Enter start year: "))
end = int(input("Enter end year: "))

years = leapyearsinrange(sr, er)

if years:
    print("Leap years between", sr, "and", er, "are:", years)
else:
    print("No leap years in this range.")

