# Function to check if a number is even
def is_even(n):
    return n % 2 == 0

# Input range from user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Even numbers in the range:")
for num in range(start, end + 1):
    if is_even(num):
        print(num, end=" ")
