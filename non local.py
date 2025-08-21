def fun1():
    a=10
    print("from fun1 a",a)

    def fun2():
        a=100
        b=20
        print("from fun2 b",b)
        print("from fun2 a",a)

    fun2()
    print("from fun1 a",a)
fun1()
