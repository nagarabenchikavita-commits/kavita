start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Even numbers:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=" ")

print("\nOdd numbers:")
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=" ")
