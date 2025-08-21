# Customized function to count digits
def countdigit(n):
    # Special case for 0
    if n == 0:
        return 1
    
    # If number is negative, make it positive
    if n < 0:
        n = -n
    
    count = 0
    while n > 0:
        n = n// 10  # Remove last digit
        count += 1             # Increase counter
    return count

# Main program
num = int(input("Enter a num: "))
res = countdigit(num)
print("Num of digits:", res)
