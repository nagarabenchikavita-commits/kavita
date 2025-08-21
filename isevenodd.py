# Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")

# Take input
num = int(input("Enter a number: "))

# Call the function
check_even_odd(num)
