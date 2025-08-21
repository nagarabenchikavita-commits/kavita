# Customized function to check Armstrong number
def is_armstrong(number):
    # Handle negative numbers (Armstrong numbers are positive by definition)
    if number < 0:
        return False

    # Count digits
    temp = number
    digits = 0
    while temp > 0:
        temp //= 10
        digits += 1

    # Calculate sum of digits raised to power
    temp = number
    armstrong_sum = 0
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** digits
        temp //= 10

    # Check if Armstrong
    return armstrong_sum == number

# Main program
num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
