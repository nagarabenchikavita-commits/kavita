def fun1():
    print("Inside fun1")

def fun2(x,y):
    z=x+y
    print("the sum is",z)

def display(ptr1,ptr2):
    ptr1()
    x=10
    y=20
    ptr2(x,y)
fun1()
fun2(15,20)

ptr3=fun1
ptr4=fun2

ptr3()
a=100
b=200
ptr4(a,b)
display(ptr3,ptr4)