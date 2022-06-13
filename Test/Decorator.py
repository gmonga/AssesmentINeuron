from decorator import decorator

#decorator changes the behaviour of the function or the call
def exampleDec(func):
    def test():
        print("This is execution of exampledec on is called on heel function")
        func()
        print("This is printed after the function is called")

    return test

# passing hello function as input to the example dec function
@exampleDec
def hello():
    print("Hello! The function is executing")


hello()