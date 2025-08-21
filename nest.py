def outer():
    print("i am outer")

    def inner():
        print("i am inner")

    inner()
outer()