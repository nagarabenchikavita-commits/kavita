def fun1():
    print("inside fun1")

def fun2(x,y):
    r1=x*y
    print("r1")

def display(ptr1,ptr2):
    ptr1()
    ptr2(50,10)
fun1()
a=10
b=5
fun2(a,b)
ptr3=fun1
ptr4=fun2
ptr3()
ptr4(10,20)
display(ptr3,ptr4)