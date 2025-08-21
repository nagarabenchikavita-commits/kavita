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
n= int(input("Enter a num: "))
temp = n
pow = countdigit(n)
asn = 0
while n > 0:
   base = n % 10
asn = asn + (base**pow)
n = n//10