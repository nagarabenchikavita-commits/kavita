def fiboseriesdecr(pos):
    n1, n2 = 0, 1
    while pos > 0:
        print(n1, end=" ")
        temp = n1 + n2
        n1 = n2
        n2 = temp
        pos -= 1

# Taking input from the user
pos = int(input("Enter the position of the Fibonacci series: "))
fiboseriesdecr(pos)
