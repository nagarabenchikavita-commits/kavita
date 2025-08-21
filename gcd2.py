def find_gcd(n1,n2):
    lower = num1
    if n2 < num1:
        lower = n2

    gcd = 1
    for i in range(2, lower + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd

# Taking input from user
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

# Calling the function
result = find_gcd(n1, n2)
print(f"The GCD of {n1} and {n2} is: {result}")

