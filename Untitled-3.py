n = int(input("Enter how many even numbers you want: "))

print("First", n, "even numbers:")
for i in range(1, n+1):
    print(i * 2, end=" ")
