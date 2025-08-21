def fiboseries_incr(pos):
    n1, n2 = 0, 1
    for i in range(pos):
        print(n1, end=" ")
        n1, n2 = n2, n1 + n2  

# Input from user
pos = int(input("Enter the number of terms for Fibonacci series: "))
fiboseries_incr(pos)
